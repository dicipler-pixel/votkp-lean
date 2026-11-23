"""Append a typeset working supplement. Requires PyMuPDF, ReportLab, Matplotlib."""
from hashlib import sha256
from pathlib import Path
from shutil import copyfile
import csv
import json
import tempfile

import matplotlib
import pymupdf as fitz
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
PREVIOUS = HERE.parent / 'v1_2_2' / 'What_the_Peel_Keeps_v1_2_2_Jeromie_Beasley.pdf'
PREVIOUS_SHA = 'd006fee8647c923b9e984d333231fe220184d28ecae77d061e051235e5ba3d88'
OUTPUT = HERE / 'What_the_Peel_Keeps_Codex_Working_Review.pdf'
WIDTH, HEIGHT = A4
LEFT = 52
RIGHT = WIDTH - LEFT
COLUMN = RIGHT - LEFT
INK = HexColor('#1d2a31')
SECONDARY = HexColor('#485b63')
ACCENT = HexColor('#9c3642')
PALE = HexColor('#f7eeef')


def assets():
    fonts = Path(matplotlib.get_data_path()) / 'fonts' / 'ttf'
    for alias, file in [('Body', 'DejaVuSerif'), ('BodyBold', 'DejaVuSerif-Bold'),
                        ('UI', 'DejaVuSans'), ('UIBold', 'DejaVuSans-Bold')]:
        pdfmetrics.registerFont(TTFont(alias, str(fonts / (file + '.ttf'))))
    result = json.loads((PROJECT / 'ptable/fair_baseline/results.json').read_text())
    profile = (HERE / 'profile.md').read_text()
    first = profile.splitlines()[0].removeprefix('### ')
    if not first or len(result['primary']['elements']) != 77:
        raise ValueError('Check manuscript draft and fair baseline inputs before building')
    return first, result


class Pages:
    def __init__(self, filename):
        self.pdf = Canvas(str(filename), pagesize=A4, invariant=1)
        self.pdf.setTitle('What the Peel Keeps | Working supplement')
        self.pdf.setAuthor('Jeromie Beasley | Codex working supplement')
        self.y = 0

    def start(self, section, title, page):
        self.y = HEIGHT - 43
        self.line('WHAT THE PEEL KEEPS', 'UIBold', 9, SECONDARY)
        self.pdf.setFillColor(SECONDARY)
        self.pdf.setFont('UI', 9)
        self.pdf.drawRightString(RIGHT, HEIGHT-43, 'WORKING SUPPLEMENT   /   23 NOVEMBER 2026')
        self.pdf.setStrokeColor(ACCENT)
        self.pdf.setLineWidth(1)
        self.pdf.line(LEFT, self.y-1, RIGHT, self.y-1)
        self.y -= 30
        self.line(section, 'UIBold', 10, ACCENT)
        self.y -= 2
        self.par(title, 'BodyBold', 20, 27, gap=14)
        self.page = page

    def line(self, text, font='UI', size=11, color=INK):
        self.pdf.setFont(font, size)
        self.pdf.setFillColor(color)
        self.pdf.drawString(LEFT, self.y, text)
        self.y -= size + 5

    def par(self, text, font='Body', size=10.2, leading=15.7, gap=10):
        style = ParagraphStyle('p', fontName=font, fontSize=size, leading=leading,
                               textColor=INK, splitLongWords=0)
        p = Paragraph(text, style)
        _, h = p.wrap(COLUMN, HEIGHT)
        p.drawOn(self.pdf, LEFT, self.y-h)
        self.y -= h + gap
        if self.y < 44:
            raise ValueError(f'Page overflow after {text[:60]} at y={self.y}')

    def heading(self, text):
        self.y -= 4
        self.line(text, 'UIBold', 11, ACCENT)

    def box(self, lines):
        height = 24 + len(lines)*20
        self.pdf.setFillColor(PALE)
        self.pdf.roundRect(LEFT, self.y-height, COLUMN, height, 4, fill=1, stroke=0)
        self.pdf.setFillColor(INK)
        self.pdf.setFont('UI', 12)
        for i, text in enumerate(lines):
            self.pdf.drawCentredString(WIDTH/2, self.y-22-i*20, text)
        self.y -= height+12

    def finish(self):
        self.pdf.setStrokeColor(HexColor('#d5dfe1'))
        self.pdf.line(LEFT, 39, RIGHT, 39)
        self.pdf.setFillColor(SECONDARY)
        self.pdf.setFont('UI', 8)
        self.pdf.drawString(LEFT, 25, 'Jeromie Beasley   ·   Elemental Peels   ·   Working copy for review')
        self.pdf.drawRightString(RIGHT, 25, str(self.page))
        self.pdf.showPage()


def score_table(p, data):
    xs = [LEFT+8, LEFT+275, LEFT+357, RIGHT-8]
    top = p.y
    p.pdf.setFillColor(PALE)
    p.pdf.rect(LEFT, top-22, COLUMN, 22, fill=1, stroke=0)
    headings = ['Nearest-neighbour reading', 'Long / 77', 'A/B / 77', 'Long* / 62']
    methods = [('Circle', 'circle'), ('Diamond', 'diamond'), ('Cube', 'cube'),
               ('Triangle family (simplex)', 'simplex'), ('Euclidean log ratios', 'log_ratio'),
               ('Standardized log energies', 'log_ie_z'), ('Published mat2vec, cosine', 'mat2vec')]
    rows = [headings]
    for name, key in methods:
        primary = data['primary']['methods'][key]['hits']
        subset = data['without_lanthanides']['methods'][key]['hits']
        rows.append([name, str(primary['long']), str(primary['short']), str(subset['long'])])
    for i, row in enumerate(rows):
        p.pdf.setFont('UIBold' if i in [0, 4] else 'UI', 9.3)
        p.pdf.setFillColor(INK)
        for j, text in enumerate(row):
            draw = p.pdf.drawRightString if j else p.pdf.drawString
            draw(xs[j], top-15-i*21, text)
    p.y -= 21*len(rows)+9


def typeset(target, title, r):
    p = Pages(target)
    p.start('I. THE PEEL PROFILE', title, 68)
    p.par('A rung compares two successive ionization energies. For eight forward rungs, '
          'write zₖ = IEₖ₊₁ / IEₖ and xₖ = ln zₖ. Each xₖ is positive. '
          'Two elements can place their largest steps in the same positions while differing in scale. '
          'The triangle-family reading asks how closely their eight positive step logs match after '
          'one rescaling of the entire second profile.')
    p.heading('Best uniform fit')
    p.par('For a second profile y, set uₖ = ln(xₖ / yₖ). Write M = maxₖ uₖ and m = minₖ uₖ. '
          'The uniform error after multiplying y by a positive constant a is the largest '
          'distance from ln a to the eight values of uₖ.')
    p.box(['Minimum over a > 0 of maxₖ |uₖ − ln a| = (M − m) / 2',
           'ln a = (M + m) / 2'])
    p.par('The two extreme values are M − m apart. Every choice of ln a lies at least half that '
          'distance from one extreme. Their midpoint attains equality and bounds every intermediate '
          'error. The implemented simplex distance M − m is twice this minimum. Multiplying all '
          'step logs by a raises all corresponding energy ratios to the power a.')
    p.heading('An exact pair the profile identifies')
    p.par('Start with alternating energy ratios (2, 3, 2, 3, 2, 3, 2, 3). Square them '
          'coordinatewise to obtain (4, 9, 4, 9, 4, 9, 4, 9). The positive log vectors '
          'are proportional, giving zero projective distance. The first ladder has zero rungs '
          'above 3 + 2√2. The second has four. The input here is a constructed pair.')
    p.heading('Retaining the actual scale')
    p.par('Store the normalized profile pₖ = xₖ / T and its total T = Σₖ xₖ = ln(IE₉ / IE₁). '
          'Each original ratio is then recovered as exp(Tpₖ). This supplies the scale that '
          'wall classification requires. The comparison above is the Hilbert projective distance '
          'on positive profiles, up to its conventional factor of two.')
    p.heading('What fitting the scale contributes')
    p.par('With the maximum error on log-step coordinates, fitting this common scale raises '
          'the displayed-column score from 56/77 to 60/77. Phosphorus, cobalt, iridium and '
          'gold gain a hit. Centering the same coordinates for Euclidean distance leaves '
          'its total at 59/77, with cobalt gaining and cerium losing one hit. These are '
          'post hoc comparisons on the existing elements.')
    p.finish()

    p.start('II. DISPLAYED ELEMENT COLUMNS', 'A fair comparison on the same 77 elements', 69)
    p.par('Fluorine through astatine each supply nine ionization energies and eight ratios. '
          'Each element selects the nearest other element by a stated distance. A hit means '
          'that neighbour shares the stored column label. All methods use the same candidates.')
    score_table(p, r)
    p.par('*Long is the mixer’s displayed long-form column. Its separate lanthanide row assigns '
          'Ce–Lu to positions 4–17. Long* removes La–Lu and recomputes neighbours. A/B merges '
          '11–17 with 1–7, respectively, retaining columns 8, 9, 10 and 18 separately.',
          font='UI', size=8.7, leading=12.8)
    p.heading('What changes when the neighbours change?')
    delta = [q for q in r['primary']['comparisons'] if q['shape']=='simplex' and q['baseline']=='log_ratio']
    dlo = {q['label']:q for q in delta}
    def ci(name, method):
        return '['+', '.join(f'{v:+.3f}' for v in dlo[name][method])+']'
    p.par('The simplex gains eight long-form hits over plain log ratios. Under 10,000 paired '
          'resamples with duplicates removed and neighbours reselected, the central 95% spread '
          f'of the recall difference is {ci("long","deletion95")}. This includes zero. '
          f'With all neighbours fixed, resampling paired query hits gives {ci("long","paired95")}. '
          'The first calculation answers Claude’s requested comparison.')
    p.par('The A/B gain is nine hits. Its deletion-and-reselection spread is '
          f'{ci("short","deletion95")}; removing the lanthanides brings the lower endpoint to zero. '
          'These are sensitivity checks within one finite roster. The observed ordering alone '
          'cannot establish performance for a new element or select the exact wall.')
    p.heading('Input check')
    n = r['archive']['energies_checked']; dif = len(r['archive']['differences'])
    p.par(f'{n-dif} of {n} displayed energies match the pinned threshold entries exactly. '
          f'The {dif} differences reflect finite displayed precision. Replaying the original '
          'archive values changes zero nearest neighbours on the full roster. Frozen mat2vec '
          'coordinates use cosine distance and encode information from the materials literature.')
    p.finish()

    p.start('III. PROSPECTIVE TESTS', 'Two calls an experiment can challenge', 70)
    p.par('The geometric wall is w = 3 + 2√2 ≈ 5.828427. A nearby comparison cutoff is '
          'c ≈ 5.837220. Predicting an energy ratio on either side requires specified '
          'charge states, ground-state assignments and uncertainty. The two cases below '
          'illustrate the difference between an open call and evidence that already runs against one.')
    p.heading('Francium · ordinary removal, Fr → Fr⁺ → Fr²⁺')
    p.par('The neutral first threshold is 4.0727411(11) eV. The next electron comes from '
          'the closed radon core of ground-state Fr⁺. The semiempirical second threshold '
          '22.4 ± 1.9 eV gives z = 5.500 centrally, with an endpoint box [5.03346, 5.96650]. '
          'That box spans the wall. The later directional forecast, inside, remains open. '
          'A measured ratio whose entire uncertainty interval is above w would defeat it.')
    p.par('With the adopted first-threshold bounds, a second threshold measured wholly '
          'between 23.73768111 and 23.77348109 eV would put the entire ratio between w and c. '
          'The helium- and neon-core openings in highly charged francium have theory-grade '
          'central ratios 3.968215 and 2.108593. Both sit well inside.')
    p.heading('Polonium · attachment, ²¹⁰Po⁻ → ²¹⁰Po → ²¹⁰Po⁺')
    p.par('The frozen call was outside. Three preliminary photodetachment fits from one '
          'IS728 campaign give ratios from 5.702820 to 5.702874, all inside. The collaboration’s '
          'newsletter predates the freeze. Published affinity theory also puts this rung inside. '
          'The fit statistics listed in the preliminary report leave systematic errors open. '
          'A final ground-state interval wholly inside would defeat the call.')
    p.heading('Review record')
    p.par('Claude requested a fair baseline and a prediction register in branch commit '
          'f85b1ee. Codex ran the comparison, prepared the register and assembled these '
          'working pages. Claude’s independent review of this supplement is pending at assembly. '
          'The original paper remains identifiable as v1.2.2, pages 1–67.')
    p.heading('Sources')
    p.par('Table v2.2 and test protocols: dicipler-pixel/votkp-lean, element-paper/loop-wall, '
          'snapshot 2361f09. The adjacent profile proof, benchmark JSON and prediction register '
          'give the inputs, uncertainty boxes, competing readings and source links. '
          'Text embeddings: Tshitoyan et al., Nature (2019), doi:10.1038/s41586-019-1335-8. '
          'CrabNet: Wang et al. (2021), doi:10.1038/s41524-021-00545-1.',font='UI',size=8.6,leading=13)
    p.finish()
    transfer = PROJECT / 'ptable/reference_transfer'
    tr = json.loads((transfer / 'results.json').read_text())
    with (transfer / 'predictions.csv').open(newline='') as stream:
        heavy_rows = [row for row in csv.DictReader(stream) if row['panel']=='heavy']
    if len(heavy_rows)!=tr['heavy']['queries']:
        raise ValueError('Transfer inputs disagree on the number of heavy queries')
    p.start('IV. REFERENCE TRANSFER', 'Can the profile recover a column in another period?', 71)
    p.par('The reference-panel design was frozen at e3367e4 before running this comparison. '
          'The atomic thresholds and target columns were already known. The protocol kept '
          'the first eight ratios from the pinned archive and excluded the detached '
          'lanthanide and actinide rows. A query must find an element in its exact long-form column.')
    p.heading('Exclude the query’s entire period')
    hist = tr['historical']
    p.par(f'Among {hist["queries"]} F–At queries, the simplex recovered {hist["simplex_hits"]} '
          f'columns and Euclidean log ratios recovered {hist["log_hits"]}. '
          f'Only the simplex succeeded for {", ".join(hist["simplex_only"])}. Only the '
          f'plain logs succeeded for {" and ".join(hist["log_only"])}. The exact two-sided '
          f'sign test on those six discordant queries gives p = {hist["descriptive_sign_p"]:.4f}.')
    p.heading('Hold the F–At reference set fixed')
    h = tr['heavy']
    p.par(f'Among eight eligible Rn–Og queries, the simplex recovered {h["simplex_hits"]} '
          f'exact columns and plain logs recovered all {h["log_hits"]}. Each query chose among '
          f'the same {h["reference_elements"]} lighter references. The p value on the '
          f'three discordant queries is {h["descriptive_sign_p"]:.2f}.')
    xs = [LEFT+7, LEFT+114, LEFT+235, LEFT+358]
    labels = ['Query', 'Simplex neighbour', 'Log-ratio neighbour', 'Input grades¹']
    rows = [labels] + [[r['symbol'],r['simplex'],r['logs'],r['grades']] for r in heavy_rows]
    top = p.y
    p.pdf.setFillColor(PALE)
    p.pdf.rect(LEFT, top-20, COLUMN, 20, fill=1, stroke=0)
    for j, row in enumerate(rows):
        p.pdf.setFillColor(INK)
        p.pdf.setFont('UIBold' if j == 0 else 'UI',9.2)
        for x, text in zip(xs,row):
            p.pdf.drawString(x,top-14-19*j,text)
    p.y -= 19*len(rows)+7
    p.par('¹ Nine removals per heavy query. E = experimental, S = semiempirical, '
          f'T = theoretical. Their {sum(h["query_thresholds"].values())} threshold entries '
          f'include {h["query_thresholds"]["E"]} E, {h["query_thresholds"]["S"]} S and '
          f'{h["query_thresholds"]["T"]} T. Requiring nine E entries left '
          f'{tr["historical_all_E"]["queries"]} historical and '
          f'{tr["heavy_all_E"]["queries"]} heavy queries. An experimental-only comparison is unavailable.',
          font='UI', size=8.7, leading=12.8)
    p.heading('What transferred')
    p.par('Rf, Db and Sg move to Ge, As and Se under the simplex. These are A/B partners '
          'in groups 4/14, 5/15 and 6/16. They still count as three errors under the frozen '
          'long-form target. Neither panel meets the specified advantage test of more '
          'simplex wins than losses and p below 0.05. The tests involve related elements '
          'and existing labels. They supply no measured-only advantage and no determination '
          'of the loop-wall cutoff.')
    p.finish()
    p.pdf.save()


def build():
    head, data = assets()
    if sha256(PREVIOUS.read_bytes()).hexdigest() != PREVIOUS_SHA:
        raise ValueError('Original manuscript fingerprint changed')
    with tempfile.TemporaryDirectory() as tmp:
        extra = Path(tmp) / 'supplement.pdf'
        typeset(extra, head, data)
        combined = Path(tmp) / 'combined.pdf'
        copyfile(PREVIOUS, combined)
        with fitz.open(combined) as document, fitz.open(extra) as new:
            if len(document)!=67 or len(new)!=4:
                raise ValueError('Unexpected number of pages')
            document.insert_pdf(new)
            document.save(combined, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP, no_new_id=True)
        with fitz.open(PREVIOUS) as old, fitz.open(combined) as review:
            for i in range(len(old)):
                if old[i].get_text()!=review[i].get_text():
                    raise ValueError(f'Original page text changed: {i+1}')
                if old[i].get_pixmap().samples!=review[i].get_pixmap().samples:
                    raise ValueError(f'Original page appearance changed: {i+1}')
            if len(review)!=71 or not combined.read_bytes().startswith(PREVIOUS.read_bytes()):
                raise ValueError('Original byte prefix or combined length changed')
        copyfile(combined, OUTPUT)
    print(f'{OUTPUT.name}: 71 pages; original 67 page texts and rasters verified.')


if __name__=='__main__':
    build()
