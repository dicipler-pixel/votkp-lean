# Brief for every VOTKP reader (11 Nov 2026)
You are reading old versions of Jeromie Beasley's VOTKP / Elemental Peeling paper (byline "Jeromie Beasley" only). Read your assigned files IN FULL, every line of text (equations, tables, captions, appendices). No skimming, no summary-instead-of-reading. If a file is too long to hold at once, read it in chunks and append notes to your output file as you go.

HOW TO GET A FILE: load the Drive tool with ToolSearch, query "select:mcp__Google_Drive__download_file_content". Call it with the fileId. The result is base64 and is saved to a file; decode it with Python into /home/claude/sm/votkp_reads/src/<label>/ (make the dir). Zip: unzip into that dir and read the paper HTML/MD/PDF inside (skip images, videos, big data). HTML: strip <script>/<style> and tags with Python (html.unescape), keep the text. PDF: use pdftotext -layout. Run Python with -I.

TODAY'S FRAME (for the "connections" section only — do not bend the reading toward it):
- One peel step of ratio z has Smith point Γ = (z−1)/(z+1) = tanh(½ ln z); its length is ln z. In Garrett's ball tree one edge is ratio 5 (Γ = 2/3).
- The half-line wall Γ² = ½ is z = 3+2√2 = 5.828: two equal perpendicular steps make a loop that closes as a pure turn inside it, parabolic on it, does not close past it. Of 5,737 ionisation steps only 8 are past it (Li, Na, K, Rb, Cs first steps; Be, B, C K-shell openings).
- At a wall the amplitude dies and the phase survives ("phase crosses what amplitude cannot"). A spin at a wall is CANCELLED (partner on the reversed word), LOCKED (resonance on a periodic end) or CONVERTED (keeps its record as a phase).
- Two books per edge: E⁻/E⁺ = Γ². The neutrino step m3/m2 sits on the wall if m1 = 0; Koide's lepton ½ is balanced books (E⁻ = E⁺).

WRITE /home/claude/sm/votkp_reads/READ_<label>.md with:
1. Coverage: each file, its version/date, characters of text read, read-in-full yes/no (yes only if every line), anything not read.
2. What the version defines and claims, section by section, with its own equation/section numbers and short exact quotes (under 15 words each).
3. EVERY ELEMENT-SPECIFIC RESULT: a table — element (symbol, Z), the quantity (IE ladder step, Γ, shell wall, closure, colour, film, phase, gap, screening constant, anything), the number, the section. List every element the version mentions with a number.
4. Bold moves: unusual mathematical connections, changes of variable, constructions or angles of attack in this version (the move itself, with its assumptions), especially ones LATER versions dropped. Not softened claims — the mathematical move.
5. Connections to today's frame: any place the version already has the wall (Γ² = ½, z ≈ 5.83, 3+2√2, √2, 1/√2), phase-at-a-wall, cancel/lock/convert, two books, a tree/ball, Lorentz/rapidity, neutrinos, Koide, spin. Quote the line.
6. Anything that contradicts today's frame.
Return a short report (under 300 words): coverage, the 3–5 strongest element results, the 2–3 boldest moves, and any connection to the wall. Do not edit any other file; do not push anything.
