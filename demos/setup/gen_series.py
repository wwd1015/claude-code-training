"""Demo 03 — many small time series, a few with injected anomalies.

Writes data/series/<id>.csv for the anomaly-triage subagent demo. Most series are clean
AR(1)-ish noise; a known subset gets a level shift or a spike. Prints the ground-truth
anomalous ids so the facilitator can verify the agent found them. Deterministic.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 23
N_SERIES = 200
LEN = 250
N_ANOMALOUS = 12
OUT = Path("data/series")


def main() -> None:
    rng = np.random.default_rng(SEED)
    OUT.mkdir(parents=True, exist_ok=True)
    dates = pd.bdate_range("2024-01-01", periods=LEN)

    anomalous = set(rng.choice(N_SERIES, N_ANOMALOUS, replace=False).tolist())
    truth = {}

    for i in range(N_SERIES):
        # AR(1) base
        x = np.zeros(LEN)
        for t in range(1, LEN):
            x[t] = 0.6 * x[t - 1] + rng.normal(0, 1.0)

        kind = "clean"
        if i in anomalous:
            if rng.random() < 0.5:
                shift = rng.integers(LEN // 2, LEN - 20)
                x[shift:] += rng.choice([-1, 1]) * rng.uniform(6, 10)
                kind = f"level_shift@{shift}"
            else:
                spike = rng.integers(20, LEN - 20)
                x[spike] += rng.choice([-1, 1]) * rng.uniform(12, 20)
                kind = f"spike@{spike}"
        truth[f"s{i:03d}"] = kind

        pd.DataFrame({"date": dates, "value": x}).to_csv(OUT / f"s{i:03d}.csv", index=False)

    pd.Series(truth).to_csv("data/series_truth.csv", header=["kind"])
    print(f"wrote {N_SERIES} series to {OUT}/  (len={LEN})")
    print(f"ground truth -> data/series_truth.csv  ({N_ANOMALOUS} anomalous)")
    print("anomalous ids:", ", ".join(sorted(k for k, v in truth.items() if v != "clean")))


if __name__ == "__main__":
    main()
