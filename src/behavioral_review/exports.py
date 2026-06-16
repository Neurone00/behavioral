from __future__ import annotations

import csv
from pathlib import Path

from behavioral_review.rollups import all_time_rollup, load_daily_history, weekly_rollup


def write_rollup_csvs(history_csv: str | Path, output_dir: str | Path) -> None:
    records = load_daily_history(history_csv)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    weekly = weekly_rollup(records)
    all_time = all_time_rollup(records)

    with (out / 'weekly-rollup.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(weekly.keys())
        writer.writerow(weekly.values())

    with (out / 'all-time-rollup.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(all_time.keys())
        writer.writerow(all_time.values())
