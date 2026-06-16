from datetime import date

from behavioral_review.rollups import DailyRecord, all_time_rollup, weekly_rollup


def sample_records():
    return [
        DailyRecord(date(2026, 5, 22), 72, 'good_day', 3, 0, 5, ''),
        DailyRecord(date(2026, 5, 23), 61, 'watch_day', 2, 1, 4, ''),
        DailyRecord(date(2026, 5, 24), 55, 'watch_day', 1, 1, 6, ''),
        DailyRecord(date(2026, 5, 25), 48, 'watch_day', 1, 2, 5, ''),
        DailyRecord(date(2026, 5, 26), 69, 'watch_day', 3, 0, 4, ''),
        DailyRecord(date(2026, 5, 27), 59, 'watch_day', 3, 1, 8, ''),
    ]


def test_weekly_rollup_sums_examples():
    summary = weekly_rollup(sample_records(), end_day=date(2026, 5, 27))
    assert summary['days_covered'] == 6
    assert summary['positive_examples'] == 13
    assert summary['negative_examples'] == 5


def test_all_time_rollup_dominant_band():
    summary = all_time_rollup(sample_records())
    assert summary['dominant_band'] == 'watch_day'
