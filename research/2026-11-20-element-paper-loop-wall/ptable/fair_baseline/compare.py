"""Reproduce the 77-element nearest-neighbour contest from pinned, local inputs."""
import csv
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
TABLE = HERE.parent / 'v2' / 'ptable_v2_data.json'
ARCHIVE = HERE.parents[3] / 'data' / 'element_thresholds_20261011.json.gz'
SHAPES = ('circle', 'diamond', 'cube', 'simplex')
RNG_SEED = 20261123
REPEATS = 10000


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def features():
    path = HERE / 'published_features.csv'
    with path.open() as file:
        reader = csv.DictReader(file)
        names = [name for name in reader.fieldnames if name != 'symbol']
        vectors = {}
        for row in reader:
            assert row['symbol'] not in vectors
            vectors[row['symbol']] = [float(row[name]) for name in names]
    assert len(names) == 200 and len(vectors) == 77
    return vectors


def load():
    rows = json.loads(TABLE.read_text())['elements']
    rows = [e for e in rows if len(e['ie']) >= 9 and e.get('col') and not e.get('heavy')]
    assert [e['Z'] for e in rows] == list(range(9, 86))
    with gzip.open(ARCHIVE, 'rt') as file:
        archive = {r['Z']: r for r in json.load(file)['records']}
    exact, discrepancies = [], []
    for row in rows:
        data = archive[row['Z']]
        assert data['symbol'] == row['sym']
        energies = {v['q']: v['IE_eV'] for v in data['thresholds']}
        exact.append([energies[q] for q in range(9)])
        for q, (rounded, full) in enumerate(zip(row['ie'][:9], exact[-1])):
            if rounded != full:
                discrepancies.append([row['sym'], q + 1, rounded, full])
    return rows, np.array(exact), discrepancies


def difference(x):
    return x[:, None] - x[None, :]


def distance_matrices(ie, vectors):
    assert ie.shape[1] == 9 and np.isfinite(ie).all()
    z = ie[:, 1:] / ie[:, :-1]
    assert (z > 1).all()
    g = (z - 1) / (z + 1)
    x = g * (0.999 / np.sqrt(z.shape[1]))
    norm = 1 - (x ** 2).sum(axis=1)
    logz = np.log(z)
    ln_ie = np.log(ie)
    scaled = (ln_ie - ln_ie.mean(axis=0)) / ln_ie.std(axis=0)
    mats = {
        'circle': np.arccosh(1 + 2 * (difference(x)**2).sum(axis=-1) / np.outer(norm, norm)),
        'diamond': np.abs(difference(logz)).sum(axis=-1) / 2,
        'cube': np.ptp(difference(np.log(np.concatenate([1-g, 1+g], axis=1))), axis=-1) / 2,
        'simplex': np.ptp(difference(np.log(logz)), axis=-1),
        'log_ratio': np.linalg.norm(difference(logz), axis=-1),
        'log_ie_z': np.linalg.norm(difference(scaled), axis=-1),
    }
    if vectors is not None:
        unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
        mats['mat2vec'] = 1 - unit @ unit.T
    for mat in mats.values():
        assert np.isfinite(mat).all() and np.allclose(mat, mat.T)
        np.fill_diagonal(mat, np.inf)
    return mats


def qinterval(values):
    return np.quantile(values, [0.025, 0.975]).tolist()


def cohort(rows, ie, external, *, statistics=True):
    symbols = np.array([e['sym'] for e in rows])
    vectors = np.array([external[s] for s in symbols]) if external else None
    mats = distance_matrices(ie, vectors)
    long = np.array([e['col'] for e in rows])
    short = np.where((long >= 11) & (long <= 17), long-10, long)
    labs = {'long': long, 'short': short}
    elements = [dict(symbol=s, Z=r['Z'], long=int(c), short=int(d))
                for s, r, c, d in zip(symbols, rows, long, short)]
    n = len(rows)
    nearest = {name: m.argmin(axis=1) for name, m in mats.items()}
    hits = {label: {name: labels == labels[index] for name, index in nearest.items()}
            for label, labels in labs.items()}
    methods = {}
    for name, idx in nearest.items():
        mat = mats[name]
        ties = np.sum(np.isclose(mat, mat[np.arange(n), idx, None], rtol=1e-12, atol=1e-14), axis=1)
        methods[name] = dict(neighbors=symbols[idx].tolist(), hits={
            label: int(hits[label][name].sum()) for label in labs
        }, tied_queries=symbols[ties > 1].tolist())
    out = dict(elements=elements, methods=methods)
    if not statistics:
        return out

    # Shared draws preserve within-element pairing across methods.
    rng = np.random.default_rng(RNG_SEED)
    draw = rng.integers(n, size=(REPEATS, n))
    perm = np.stack([rng.permutation(n) for _ in range(REPEATS)])
    baselines = [m for m in mats if m not in SHAPES]
    # Re-run every neighbour search after deletion, as in Claude's original.
    # Every retained element counts once; feature scaling stays fixed at full-cohort values.
    names = list(mats)
    deleted = {label: np.empty((REPEATS, len(names))) for label in labs}
    for r, indices in enumerate(draw):
        keep = np.unique(indices)
        for m, name in enumerate(names):
            near = keep[mats[name][np.ix_(keep, keep)].argmin(axis=1)]
            for label, labels in labs.items():
                deleted[label][r,m] = np.mean(labels[keep] == labels[near])
    comparisons, shuffled, chance = [], {}, {}
    for label, labels in labs.items():
        counts = np.unique(labels, return_counts=True)[1]
        chance[label] = np.sum(counts * (counts - 1)).item() / (n * (n - 1))
        permuted = labels[perm]
        shuffled[label] = {}
        for name, idx in nearest.items():
            scores = (permuted == permuted[:, idx]).mean(axis=1)
            observed = hits[label][name].mean()
            shuffled[label][name] = dict(
                mean=float(scores.mean()), p99=float(np.quantile(scores, 0.99)),
                p_upper=(1+int(np.sum(scores >= observed))) / (1+REPEATS))
        for shape in SHAPES:
            for base in baselines:
                diff = hits[label][shape].astype(int) - hits[label][base].astype(int)
                paired = diff[draw].mean(axis=1)
                deletion = deleted[label][:, names.index(shape)] - deleted[label][:, names.index(base)]
                comparisons.append(dict(label=label, shape=shape, baseline=base,
                    delta=float(diff.mean()), paired95=qinterval(paired), deletion95=qinterval(deletion),
                    shape_only=int(sum(diff > 0)), baseline_only=int(sum(diff < 0))))
    out.update(comparisons=comparisons, shuffled=shuffled, chance=chance)
    return out


def main():
    rows, exact, diffs = load()
    ext = features()
    ie = np.array([e['ie'][:9] for e in rows])
    main = cohort(rows, ie, ext)
    assert [main['methods'][m]['hits']['long'] for m in SHAPES] == [53,52,48,60]
    keep = np.array([not 57 <= e['Z'] <= 71 for e in rows])
    sensitivity = cohort([e for e,k in zip(rows,keep) if k], ie[keep], ext)
    replay = cohort(rows, exact, ext, statistics=False)
    archive_changes = {}
    for mode in main['methods']:
        before = main['methods'][mode]
        after = replay['methods'][mode]
        archive_changes[mode] = dict(hits=after['hits'], changed_neighbors=[
            [e['sym'],i,j] for e,i,j in zip(rows,before['neighbors'],after['neighbors']) if i != j])
    hashes = {'table':sha(TABLE), 'archive':sha(ARCHIVE)}
    hashes['published_features'] = sha(HERE / 'published_features.csv')
    result = dict(source_sha256=hashes, numpy=np.__version__, seed=RNG_SEED, draws=REPEATS,
                  primary=main, without_lanthanides=sensitivity,
                  archive=dict(energies_checked=ie.size, differences=diffs, replay=archive_changes))
    (HERE / 'results.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
