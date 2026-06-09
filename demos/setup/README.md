# Demo data generators

Zero-infra synthetic data so every demo runs on a laptop with no internal access. All
generators are deterministic (seeded) and write to `./data/` (git-ignored — data is never
committed).

## Install
```bash
pip install -r requirements.txt
```

## Generate everything
```bash
python gen_sample_dataset.py     # -> data/sample.parquet, data/sample.csv     (Demo 01)
python gen_backtest_results.py   # -> data/results.parquet                     (Demo 02)
python gen_series.py             # -> data/series/*.csv (with injected anomalies)(Demo 03)
python gen_warehouse.py          # -> data/warehouse.duckdb                     (Demo 04)
```

Each generator prints what it wrote and, where relevant, where the "right answers" are
(injected anomalies, the leaked column) so the facilitator can confirm the demo lands.
