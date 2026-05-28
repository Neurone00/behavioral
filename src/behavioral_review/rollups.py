from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


@dataclass(frozen=True)
class DailyRecord:
    day: date
    daily_score: int
    band: str
    positive_examples: int
    negative_examples: int
    neutral_examples: int
    notes: str


def load_daily_history(csv_path: str | Path) -> list[DailyRecord]:
    path = Path(csv_path)
    if not path.exists():
        return []
    rows = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(
                DailyRecord(
                    day=date.fromisoformat(row["date"]),
                    daily_score=int(row["daily_score"]),
                    band=row["band"],
                    positive_examples=int(row["positive_examples"]),
                    negative_examples=int(row["negative_examples"]),
                    neutral_examples=int(row["neutral_examples"]),
                    notes=row["notes"],
                )
            )
    return rows


def weekly_rollup(records: list[DailyRecord], end_day: date | None = None) -> dict[str, int | str]:
    if not records:
        return {
            "days_covered": 0,
            "average_score": 0,
            "positive_examples": 0,
            "negative_examples": 0,
            "neutral_examples": 0,
            "dominant_band": "no_data",
        }

    last_day = end_day or max(record.day for record in records)
    start_day = last_day - timedelta(days=6)
    scoped = [record for record in records if start_day <= record.day <= last_day]
    return summarize_records(scoped)


def all_time_rollup(records: list[DailyRecord]) -> dict[str, int | str]:
    return summarize_records(records)


def summarize_records(records: list[DailyRecord]) -> dict[str, int | str]:
    if not records:
        return {
            "days_covered": 0,
            "average_score": 0,
            "positive_examples": 0,
            "negative_examples": 0,
            "neutral_examples": 0,
            "dominant_band": "no_data",
        }

    count = len(records)
    bands = Counter(record.band for record in records)
    return {
        "days_covered": count,
        "average_score": round(sum(record.daily_score for record in records) / count),
        "positive_examples": sum(record.positive_examples for record in records),
        "negative_examples": sum(record.negative_examples for record in records),
        "neutral_examples": sum(record.neutral_examples for record in records),
        "dominant_band": bands.most_common(1)[0][0],
    }
