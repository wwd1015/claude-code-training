"""Demo 04 — local DuckDB 'warehouse' for the SQL-over-MCP demo.

Builds data/warehouse.duckdb with a couple of tables a quant would actually query, so the
MCP demo (NL -> SQL -> result -> chart) has real structure. Zero credentials. Deterministic.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 31
OUT = Path("data")


def main() -> None:
    try:
        import duckdb
    except ImportError:
        raise SystemExit("duckdb not installed — run: pip install duckdb")

    rng = np.random.default_rng(SEED)
    OUT.mkdir(exist_ok=True)

    dates = pd.bdate_range("2024-01-01", "2024-12-31")
    symbols = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    rows = []
    for sym in symbols:
        price = 100 + np.cumsum(rng.normal(0, 1, len(dates)))
        vol = rng.lognormal(13, 0.4, len(dates)).astype(int)
        # inject a couple of high-volume days for the demo question
        vol[rng.integers(0, len(dates), 3)] *= 6
        for d, p, v in zip(dates, price, vol):
            rows.append((d.date(), sym, round(float(p), 2), int(v)))
    trades = pd.DataFrame(rows, columns=["date", "symbol", "close", "volume"])

    db = OUT / "warehouse.duckdb"
    con = duckdb.connect(str(db))
    con.execute("CREATE OR REPLACE TABLE trades AS SELECT * FROM trades")
    con.execute(
        "CREATE OR REPLACE VIEW daily_volume AS "
        "SELECT date, sum(volume) AS total_volume FROM trades GROUP BY date ORDER BY date"
    )
    con.close()
    print(f"wrote {db}  (tables: trades [{len(trades)} rows], view: daily_volume)")
    print(
        "demo question to try: 'top 10 days by total volume in Q4, and plot the daily series'"
    )


if __name__ == "__main__":
    main()
