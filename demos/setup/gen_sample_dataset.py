"""Demo 01 — messy unfamiliar dataset for the EDA + data-dictionary demo.

Deliberately includes the things /eda should catch: nulls, an ID column, a date column,
numeric outliers, a high-cardinality categorical, a near-all-null column, mixed types,
and a *leaked target* (a column that trivially predicts `target`). Deterministic.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 7
N = 5000
OUT = Path("data")


def main() -> None:
    rng = np.random.default_rng(SEED)
    OUT.mkdir(exist_ok=True)

    dates = pd.to_datetime("2024-01-01") + pd.to_timedelta(
        rng.integers(0, 540, N), unit="D"
    )
    region = rng.choice(["NA", "EMEA", "APAC", "LATAM"], N, p=[0.45, 0.3, 0.2, 0.05])
    # a numeric with heavy right tail + a few extreme outliers
    notional = rng.lognormal(mean=11, sigma=1.0, size=N)
    notional[rng.integers(0, N, 8)] *= 50  # injected outliers

    pnl = rng.normal(0, 1500, N) + (region == "NA") * 400
    target = (pnl > 0).astype(int)

    # object-dtype column that is ~all null (np.where can't mix str+nan in modern numpy)
    legacy_flag = np.full(N, np.nan, dtype=object)
    legacy_flag[rng.random(N) < 0.02] = "Y"

    df = pd.DataFrame(
        {
            "trade_id": [f"T{100000 + i}" for i in range(N)],  # identifier
            "as_of_date": dates,  # datetime
            "region": region,  # categorical
            "desk": rng.choice(
                [f"desk_{i:03d}" for i in range(220)], N
            ),  # high-cardinality
            "notional": notional,  # outliers
            "pnl": pnl,
            "fee_bps": rng.normal(2.5, 0.4, N),
            "comment": rng.choice(
                ["", "", "", "check", "manual adj"], N
            ),  # mostly empty
            "legacy_flag": legacy_flag,  # ~all null
            "pnl_sign": np.where(pnl > 0, "up", "down"),  # LEAKED: trivially => target
            "target": target,
        }
    )

    # inject missingness
    for col, frac in [("fee_bps", 0.07), ("region", 0.03), ("notional", 0.01)]:
        idx = rng.choice(N, int(N * frac), replace=False)
        df.loc[idx, col] = np.nan

    df.to_parquet(OUT / "sample.parquet", index=False)
    df.to_csv(OUT / "sample.csv", index=False)
    print(f"wrote {OUT / 'sample.parquet'} and .csv  shape={df.shape}")
    print("facilitator notes:")
    print("  - leaked target column: 'pnl_sign' (perfectly predicts 'target')")
    print("  - near-all-null column: 'legacy_flag'")
    print("  - high-cardinality categorical: 'desk' (~220 values)")
    print("  - outliers injected into: 'notional'")


if __name__ == "__main__":
    main()
