# SCRIPT: UPDATE-WORK-ATLAS
# Jeromie Beasley's work atlas: one cross-reference of every result across his papers and Lean repos.
#
# What it does, every run:
#   1. pulls every public Lean repo listed in repos.json (and the extra branches named there);
#   2. reads every .lean file and indexes each declaration (theorem, lemma, def, ...) under its full
#      name, with file and line, and counts sorry / admit / axiom;
#   3. loads every result entry in entries/*.json and checks that each cited Lean theorem still
#      exists where it says (repo, branch, name) -- a renamed or deleted theorem is flagged, never hidden;
#   4. checks every link points at an entry that exists (or is marked external);
#   5. writes atlas.json (machine record), ATLAS.html (the readable, searchable page) and
#      STATUS.md (what needs attention).
# Usage: python3 update_atlas.py [--offline]   (offline = reuse the clones already in src/)
# It never pushes to the Lean repos; it only reads them. Proof checking itself is each repo's own CI.
import json, os, re, subprocess, sys, glob, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
OFFLINE = '--offline' in sys.argv
cfg = json.load(open(os.path.join(ROOT, 'repos.json')))
OWNER = cfg['owner']

def sh(args, cwd=None):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)

def fetch(repo, branch=None):
    d = os.path.join(SRC, repo + ('@' + branch.replace('/', '__') if branch else ''))
    url = f'https://github.com/{OWNER}/{repo}.git'
    if OFFLINE and os.path.isdir(d):
        pass
    elif os.path.isdir(os.path.join(d, '.git')):
        sh(['git', 'fetch', '-q', '--depth', '1', 'origin'] + ([branch] if branch else []), cwd=d)
        sh(['git', 'reset', '-q', '--hard', 'FETCH_HEAD'], cwd=d)
    else:
        a = ['git', 'clone', '-q', '--depth', '1'] + (['--branch', branch] if branch else []) + [url, d]
        r = sh(a)
        if r.returncode != 0:
            return None, r.stderr.strip()[:200]
    head = sh(['git', 'rev-parse', 'HEAD'], cwd=d).stdout.strip()
    br = branch or sh(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=d).stdout.strip()
    return {'dir': d, 'sha': head, 'branch': br}, None

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|unsafe|partial|nonrec)\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive|class|axiom|opaque|example)\s+([^\s:(\[{]+)?')
NS_OPEN = re.compile(r'^\s*namespace\s+(\S+)')
SEC_OPEN = re.compile(r'^\s*(?:noncomputable\s+)?section(?:\s+(\S+))?\s*$')
END = re.compile(r'^\s*end(?:\s+(\S+))?\s*$')

def strip_comments(text):
    text = re.sub(r'/-.*?-/', lambda m: '\n' * m.group(0).count('\n'), text, flags=re.S)
    return '\n'.join(l.split('--')[0] for l in text.split('\n'))

def index_repo(info):
    decls, sorries, axioms, files = [], 0, [], 0
    template = 0
    for f in glob.glob(os.path.join(info['dir'], '**', '*.lean'), recursive=True):
        rel = os.path.relpath(f, info['dir'])
        if rel.startswith('.lake') or '/.lake/' in rel or rel.startswith('lake-packages'):
            continue
        files += 1
        try:
            raw = open(f, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        text = strip_comments(raw)
        stack = []
        for ln, line in enumerate(text.split('\n'), 1):
            m = NS_OPEN.match(line)
            if m:
                stack.append(('ns', m.group(1))); continue
            m = SEC_OPEN.match(line)
            if m:
                stack.append(('sec', m.group(1) or '')); continue
            m = END.match(line)
            if m and stack:
                stack.pop(); continue
            m = DECL.match(line)
            if m and m.group(2):
                kind, name = m.group(1), m.group(2)
                ns = '.'.join(s[1] for s in stack if s[0] == 'ns')
                full = name[1:] if name.startswith('_root_.') else (ns + '.' + name if ns else name)
                decls.append({'name': full, 'short': name.split('.')[-1], 'kind': kind, 'file': rel, 'line': ln})
                if kind == 'axiom':
                    axioms.append(full)
            n = len(re.findall(r'\bsorry\b|\badmit\b', re.sub(r'`[^`]*`', '', line)))
            if re.search(r'Statements|selftest|FalseControl', rel): template += n
            else: sorries += n
    return decls, sorries, axioms, files, template

def main():
    os.makedirs(SRC, exist_ok=True)
    index, repos_out = {}, []
    targets = [(r['name'], None) for r in cfg['repos']]
    for repo, brs in cfg.get('extra_branches', {}).items():
        targets += [(repo, b) for b in brs]
    for repo, branch in targets:
        info, err = fetch(repo, branch)
        key = repo + ('@' + branch if branch else '')
        if not info:
            repos_out.append({'repo': repo, 'branch': branch, 'error': err}); continue
        decls, sorries, axioms, files, template = index_repo(info)
        index[key] = decls
        if not branch:
            index[repo + '@' + info['branch']] = decls
        repos_out.append({'repo': repo, 'branch': info['branch'], 'sha': info['sha'][:10], 'lean_files': files,
                          'declarations': len(decls), 'theorems': sum(1 for d in decls if d['kind'] in ('theorem', 'lemma')),
                          'sorry_or_admit': sorries, 'open_statement_templates': template, 'axioms': axioms})
        print(f'{key:55s} {len(decls):5d} decls  sorry {sorries}', flush=True)

    entries = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'entries', '*.json'))):
        for e in json.load(open(f)):
            e['_file'] = os.path.basename(f); entries.append(e)
    ids = {e['id'] for e in entries}
    problems = []
    for e in entries:
        L = e.get('lean')
        e['lean_status'] = 'no Lean proof cited'
        if L and L.get('theorem'):
            keys = [L['repo'].split('/')[-1] + '@' + L['branch']] if L.get('branch') else []
            keys += [k for k in index if k.split('@')[0] == L['repo'].split('/')[-1]]
            hit = None
            for k in keys:
                for d in index.get(k, []):
                    if d['name'] == L['theorem'] or d['name'].endswith('.' + L['theorem']) or d['short'] == L['theorem']:
                        if not L.get('file') or d['file'] == L['file'] or d['file'].endswith(L['file']):
                            hit = (k, d); break
                if hit: break
            if hit:
                k, d = hit
                e['lean_status'] = 'found'
                e['lean_found'] = {'where': k, 'file': d['file'], 'line': d['line'], 'name': d['name']}
            else:
                e['lean_status'] = 'MISSING'
                problems.append(f"{e['id']}: cited Lean theorem `{L['theorem']}` not found in {L['repo']} {L.get('branch') or ''} {L.get('file') or ''}")
        for l in e.get('links', []):
            if l.get('to') and '.' in l['to'] and not l['to'].startswith('external:') and l['to'] not in ids:
                l['status'] = 'dangling'
                problems.append(f"{e['id']}: link to `{l['to']}` points at no entry yet")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    out = {'updated': stamp, 'repos': repos_out, 'entries': entries, 'problems': problems}
    json.dump(out, open(os.path.join(ROOT, 'atlas.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(index, open(os.path.join(ROOT, 'lean_index.json'), 'w'), ensure_ascii=False)
    write_status(out); write_html(out)
    print(f'{len(entries)} entries, {sum(1 for e in entries if e["lean_status"]=="found")} Lean links found, {len(problems)} problems')

def write_status(o):
    s = [f"# Work atlas status — {o['updated']}", '',
         f"{len(o['entries'])} results, {sum(1 for e in o['entries'] if e['lean_status']=='found')} with a Lean proof found, "
         f"{len(o['problems'])} need attention.", '', '## Needs attention', '']
    s += [f'- {p}' for p in o['problems']] or ['- nothing']
    s += ['', '## Repos read', '', '| repo | branch | commit | Lean files | theorems | sorry/admit | axioms |', '|---|---|---|---|---|---|---|']
    for r in o['repos']:
        if r.get('error'):
            s.append(f"| {r['repo']} | {r.get('branch') or ''} | not reached: {r['error']} | | | | |")
        else:
            s.append(f"| {r['repo']} | {r['branch']} | {r['sha']} | {r['lean_files']} | {r['theorems']} | {r['sorry_or_admit']} | {len(r['axioms'])} |")
    open(os.path.join(ROOT, 'STATUS.md'), 'w').write('\n'.join(s) + '\n')

def write_html(o):
    data = json.dumps({'updated': o['updated'], 'entries': [{k: v for k, v in e.items() if k != '_file'} for e in o['entries']],
                       'repos': o['repos'], 'problems': o['problems'], 'owner': OWNER}, ensure_ascii=False).replace('</', '<\\/')
    page = open(os.path.join(ROOT, 'atlas_template.html'), encoding='utf-8').read().replace('/*__ATLAS_DATA__*/null', data)
    open(os.path.join(ROOT, 'ATLAS.html'), 'w', encoding='utf-8').write(page)

if __name__ == '__main__':
    main()
