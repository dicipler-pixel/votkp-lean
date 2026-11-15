# VOTKP v3.0 — code added to the v2.9 package (12 November 2026)
Jeromie Beasley. Prepared with AI assistance (Claude, Anthropic).

The v2.9 package (VOTKP_v2_9_Code_Proofs_Data_20261013.zip) is unchanged and still required. These files are the additions for Sections 22-24.

- shell_screen_04.py / .out : the split in charges, the alkali charge ratio, the helium-core series and its opposite (Sections 22.3, 23.3, 23.4).
- esr_check_01.py / .out : census of the 118-element archive and the half-line counts in exact rational arithmetic (Section 23.1, Appendix D).
- figs_v30.py : Figures 35 and 36.
- build_v30.py : inserts the new sections into the complete v2.9 page; no v2.9 text is removed.

Run: python3 shell_screen_04.py element_thresholds_20261011.json.gz
The other scripts named in Appendix F are in the votkp-lean repository under research/2026-11-10 and research/2026-11-11-standard-model-ball.
