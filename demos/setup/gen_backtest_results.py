"""Demo 02 — synthetic backtest result for the /backtest-report skill demo.

A daily strategy with modest positive drift, vol clustering, and a drawdown period so the
report has something to show (Sharpe, Sortino, max drawdown, monthly heatmap). Deterministic.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 11
OUT = Path("data")


def main() -> None:
    rng = np.random.default_rng(SEED)
    OUT.mkdir(exist_ok=True)

    dates = pd.bdate_range("2019-01-01", "2024-12-31")
    n = len(dates)

    # vol clustering via a slow-moving sigma, plus a deliberate drawdown stretch
    base_sigma = 0.008 + 0.004 * np.abs(np.sin(np.linspace(0, 6 * np.pi, n)))
    drift = np.full(n, 0.0004)
    dd_start, dd_end = int(n * 0.55), int(n * 0.68)
    drift[dd_start:dd_end] = -0.0010  # the drawdown

    returns = rng.normal(drift, base_sigma)
    position = np.sign(rng.normal(0.2, 1.0, n))  # mostly long, flips sometimes

    df = pd.DataFrame({"date": dates, "returns": returns, "position": position})
    df["pnl"] = df["returns"]  # alias some teams use
    df.to_parquet(OUT / "results.parquet", index=False)

    eq = (1 + df["returns"]).cumprod()
    cagr = eq.iloc[-1] ** (252 / n) - 1
    sharpe = df["returns"].mean() / df["returns"].std() * np.sqrt(252)
    mdd = (eq / eq.cummax() - 1).min()
    print(f"wrote {OUT / 'results.parquet'}  rows={n}")
    print(f"facilitator sanity: CAGR~{cagr:.1%}  Sharpe~{sharpe:.2f}  maxDD~{mdd:.1%}")
    print(
        f"  drawdown window injected around {dates[dd_start].date()}..{dates[dd_end].date()}"
    )


if __name__ == "__main__":
    main()
