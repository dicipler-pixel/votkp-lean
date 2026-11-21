# What the paired reflection measures in two isobar chains

At a common initial ionic charge $q$, take $a=IE_{q+1}$ of the higher-$Z$ isotope's element and $b=IE_{q+1}$ of the lower-$Z$ isotope's element. Order the mass difference in the same way, $Q(q)=[M_H(q)-M_L(q)]c^2$. The two-species ratio $z=a/b$ gives precisely the VOTKP reflection

$$\rho_q=\frac{a-b}{a+b}=\frac{z-1}{z+1}.$$

**DERIVED.** Equal charge cancels the removed-electron rest energy. Therefore $Q(q+1)-Q(q)=a-b=\rho_q(a+b)$, and for every finite initial segment

$$Q(n)=Q(0)+\sum_{q=0}^{n-1} \rho_q\bigl(IE_{H,q+1}+IE_{L,q+1}\bigr).$$

Reversing the order of the two species flips $\rho_q$ and preserves its positive energy weight. Thus $\rho_q$ gives the direction of the **increment** exactly. Testing whether $\rho_q$ alone supplies the sign of the accumulated mass difference requires both signs to agree after every step. The pinned central data falsify that test on both chains. They agree only 49/66 times for holmium/dysprosium and 53/81 times for lead/thallium, counting an exact zero increment separately from either sign. The weighted, anchored sum itself reproduces every central gap. These identities provide energy accounting. A decay rate additionally requires an accessible electronic and nuclear transition.

| Isobars and decisive charge step | Higher/lower next thresholds | Paired reflection | Weighted increment | Ground-mass difference before → after |
|---|---|---|---:|---|
| ¹⁶³Ho / ¹⁶³Dy, 56 → 57 | 5,611 / 12,081 eV | −3235/8846 | −6,470 eV | +1,951.406439 → −4,518.593561 eV |
| ²⁰⁵Pb / ²⁰⁵Tl, 79 → 80 | 24,938.2 / 96,783.2 eV | −359225/608607 | −71,845 eV | +37,544.790452 → −34,300.209548 eV |

Both paired reflection powers are below one half. These numerical reversals concern the accumulated same-charge ground-mass ordering. The table uses element-reference ionization energies, isotope-specific neutral anchors and the indicated sign convention. The intermediate charges are calculations. [Holmium/dysprosium source and uncertainty ledger](../materials/holmium_dysprosium_decay.md) · [Lead/thallium source and uncertainty ledger](../../batch17/materials/tl_pb_decay.md)

At the last lead/thallium step the paired reflection changes back to positive, with increment +899.68 eV, while $Q(81)$ remains negative at −33,400.5295484 eV. The predicted release to the first excited lead state is $33,400.5295484-2,329=31,071.5295484$ eV. The storage-ring paper reports a 31.1(5) keV bound-state beta energy from its electronic and nuclear inputs. Its measured decay supplies a physical endpoint with a specified daughter state. The agreement uses related atomic inputs and does not constitute a separate lifetime prediction. [Leckenby et al., Nature (2024), Methods Eq. 3](https://doi.org/10.1038/s41586-024-08130-4)

The rational proofs live in [Weighted.lean](Weighted.lean). The [verification script](verify_weighted.py) checks the 147 increments against the two existing ledgers from the pinned archive, then builds the proofs with Lean 4.34.1.
