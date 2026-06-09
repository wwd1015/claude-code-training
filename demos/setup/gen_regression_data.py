"""Demo 06 — synthetic econometric dataset for the /regression-diagnostics demo (Quant seed).

Includes the pathologies a quant's diagnostics should catch: known coefficients, strong
multicollinearity (high VIF), heteroskedastic errors (Breusch-Pagan), and a non-stationary
(unit-root) column for an ADF test. Deterministic.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 41
N = 600
OUT = Path("data")


def main() -> None:
    rng = np.random.default_rng(SEED)
    OUT.mkdir(exist_ok=True)

    x1 = rng.normal(0, 1, N)
    x2 = rng.normal(0, 1, N)
    # multicollinearity: x3 ~ x1 (corr ~0.97) -> high VIF on x1 and x3
    x3 = x1 * 0.95 + rng.normal(0, 0.2, N)

    b0, b1, b2, b3 = 1.0, 2.0, -1.5, 0.5
    # heteroskedastic noise: error variance grows *monotonically* with x1, so a standard
    # (linear) Breusch-Pagan test against x1 detects it. (Variance ~ |x1| would be symmetric
    # and BP would miss it — a deliberately detectable pathology here.)
    sigma = 0.4 + 0.5 * (x1 - x1.min())
    eps = rng.normal(0, sigma)
    y = b0 + b1 * x1 + b2 * x2 + b3 * x3 + eps

    # a non-stationary (random-walk / unit-root) regressor for an ADF demo
    rw = np.cumsum(rng.normal(0, 1, N))

    df = pd.DataFrame({"y": y, "x1": x1, "x2": x2, "x3": x3, "rw_unit_root": rw})
    df.to_parquet(OUT / "econ_panel.parquet", index=False)
    df.to_csv(OUT / "econ_panel.csv", index=False)
    print(f"wrote {OUT / 'econ_panel.parquet'} and .csv  shape={df.shape}")
    print("facilitator notes (diagnostics should surface these):")
    print(f"  - true coefficients: b0={b0} b1={b1} b2={b2} b3={b3}")
    print("  - multicollinearity: x3 ~= 0.95*x1  -> high VIF on x1, x3")
    print("  - heteroskedasticity: error variance grows with x1 -> Breusch-Pagan should reject")
    print("  - non-stationary column: 'rw_unit_root' -> ADF should NOT reject the unit root")


if __name__ == "__main__":
    main()
