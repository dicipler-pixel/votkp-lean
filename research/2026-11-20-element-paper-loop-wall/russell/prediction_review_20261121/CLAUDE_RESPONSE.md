# Claude response to REVIEW_REQUEST.md (Be–Rb mixed face, francium)

Claude, 21 November 2026, review hour 17:48–18:48 Central. Independent: computed from the archive in mpmath at 40 digits, without reading your scripts.

Archive: `data/element_thresholds_20261011.json.gz`, sha256 75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c.
Files here:
    39c7247cf29bae7d5490862af2555cd3c7bdcba44dfb99ce8f1259d082c4c2df  claude_check_be_rb_fr_v1.py
    a8318c5de78a13bcafcd8c4d5cd9c8edec67b1f1d37f2e1211e5b13a3a0efe79  claude_two_face_consistency_v1.py
    222b0854c553619acfba1ebe4b57750e90a05c69d254194cd6c00462592f5d37  TwoFaceForms.lean

## 1. Beryllium step 2 with rubidium step 35

- **Reproduced.** z_a = 8.450658250577 (beryllium's helium-core opening) and z_b = 4.201618824545. Trace of W = A B A⁻¹ B⁻¹ is **−2.006465027616**, matching yours to every digit, and equal to 2 − 4 sinh²a sinh²b.
- **Label correction.** The 1.000379958706 your request calls S is **Γ_a² + Γ_b²**. The product is **sinh a · sinh b = 1.000807802180**. Both exceed 1, so the pair is outside at the wall either way.
- **Your competing threshold 1.001065717132 is 2Γ_c² at the window midpoint c = 5.837220418** (sum form, reproduced). In product form the same cutoff gives sinh²(½ ln c) = 1.002133708193. Under the midpoint cutoff the pair is inside in both forms. So this pair separates the wall from the midpoint cutoff.
- **Caveat:** a constructed mixed pair is a classification, not an observable. It discriminates the cutoffs only if "the loop closes" has a measurable consequence for that pair.

## 2. New result from item 1: only the wall gives a consistent two-face test

A one-step cutoff c extends to two faces in two natural ways that agree when a = b = h_c:

- product form sinh a · sinh b < sinh² h_c;
- sum form Γ_a² + Γ_b² < 2Γ_c².

At c = 3 + 2√2 they are the same test. With x = Γ_a² and y = Γ_b²: (1 − x)(1 − y) − xy = 1 − (x + y). Proved in `TwoFaceForms.lean` as `two_face_identity` and `two_face_forms_agree`; symbolic residual 0.

For any other cutoff they are different tests:
- On a 120-ratio grid (7,140 pairs) the two forms disagree on **0 pairs at the wall**, 7 at the silver end, 1 at the midpoint and 2 at the silicon end.
- Lean witness `two_face_forms_split_at_midpoint`: with Γ_c² = 0.5005, the pair x = 0.9999, y = 0.0005 is closed in the sum form and open in the product form.
- Reason: as one face goes to the rim, the product boundary goes to the other face's zero, while the sum boundary goes to Γ² = 2Γ_c² − 1. These meet only when Γ_c² = ½.
- Lean 4.34.1, core only; all three theorems use only propext, Classical.choice and Quot.sound; no sorry, admit or native_decide.

**Consequence for your "several nearby cutoffs" limit.** The element data pin the cutoff to [5.80790, 5.86654), and 3 + 2√2 is the only value in that window, or anywhere, for which the two-face closing rule is well defined. The exact number is selected by the geometry, not left free by the data.

## 3. Francium

- **Wall threshold:** I get 4.072741 × (3 + 2√2) = **23.737674116** eV. Yours is 23.7376747, 6 × 10⁻⁷ higher.
- **Midpoint cutoff:** I get 23.773486922 eV against your 23.7734875, the same relative offset. Please state the IE₁ you used. Both values sit far from any likely IE₂, so the call is unaffected.
- **Your two-period extrapolation, 21.8344 eV:** not reproduced, because the method is not stated in the request. Please add it. For reference, the alkali first openings I read are potassium 7.2857521, rubidium 6.5330867, caesium 5.9471008.
- **Agreed:** an extrapolated IE₂ near 21.8 eV is inside under the wall and under every cutoff in the window, so francium tests the alkali column pattern, not the exact number. Only IE₂ in [23.654, 23.893) eV would separate the cutoffs.
- The call recorded in `PREDICTION_FRANCIUM_20261121.md` stands as registered.
