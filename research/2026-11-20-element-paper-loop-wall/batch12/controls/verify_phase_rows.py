"""Cross-check directional phase data with independently summed real-space blocks."""
import csv
from pathlib import Path

import numpy as np

from verify_material_weights import read_weights

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/"localization"


def main():
    with (SOURCE/"phase_directions.csv").open() as f:
        directions=list(csv.DictReader(f))
    checked=[]
    for row in directions:
        # Default NC and smooth PAW have published full X(R) cubes.
        family={"default":"NC","smooth_PAW":"PAW"}.get(row["series"])
        if family is None:
            continue
        sym,mesh=row["symbol"],int(row["mesh"])
        path=SOURCE/"weights"/f"{family}-{sym}-{mesh}.csv"
        if not path.is_file():
            continue
        weights,cell,nu=read_weights(path)
        convention_atoms=2 if sym=="Rb" else 4
        a=(abs(np.linalg.det(cell))*convention_atoms)**(1/3)
        q=2*np.pi*np.array([int(row[key]) for key in ("h","k","l")])/(a*mesh)
        qmag=np.linalg.norm(q)
        np.testing.assert_allclose(qmag,float(row["q_inv_A"]),rtol=2e-12)
        # Direct Cartesian q·R with full unwrapped site positions is periodic.
        coords=np.array(list(np.ndindex(weights.shape)))
        phase=(coords@cell)@q
        site=(weights.ravel()@(2*np.sin(phase/2)**2))/(nu*qmag**2)
        full=float(row["microscopic_L_A2"])
        floor=float(row["rank_change_A2"])
        np.testing.assert_allclose(site,float(row["WS_phase_L_A2"]),rtol=2e-9,atol=2e-9)
        np.testing.assert_allclose(full-floor,float(row["overlap_loss_A2"]),rtol=2e-9,atol=2e-9)
        if min(site,full)+1e-9<floor:
            raise AssertionError("violated common rank floor")
        radius=a*(np.sqrt(5)/4 if sym=="Rb" else 1/2)
        miss=floor*qmag**2
        # Sum of min(source rank,target rank) divided by total source rank.
        match=1-miss
        if not 0<=match<=1:
            raise AssertionError("invalid rank budget")
        diff=abs(np.sqrt(max(0,full-floor))-np.sqrt(max(0,site-floor)))
        refined_bound=radius*np.sqrt(match)
        if diff>refined_bound+1e-8:
            raise AssertionError("violated residual bound")
        checked.append((family,sym,mesh,row['shell'],row['h'],row['k'],row['l'],
                        site,full,floor,site-floor,full-floor,diff,refined_bound))
    if not checked:
        raise ValueError("No matched real-space and phase records")
    with (HERE/"phase_rows_check.csv").open("w",newline="") as f:
        writer=csv.writer(f,lineterminator="\n");writer.writerow(("family","symbol","mesh","shell","h","k","l","WS_chord_A2",
            "full_L_A2","rank_floor_A2","WS_texture_A2","full_texture_A2","texture_root_delta_A","texture_root_bound_A"))
        for row in checked:
            writer.writerow((*row[:7],*(f"{v:.9f}" for v in row[7:])))


if __name__=="__main__":
    main()
