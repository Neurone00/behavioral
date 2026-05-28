# Spreadsheet Data Model

This document explains the intended Google Sheets workbook structure for the
behavioral review outputs.

## Goals

The workbook should make three things obvious:

- what was scored
- how it was scored
- which tabs are source data versus summary views

## Tab Layout

### `dashboard`

Purpose: fast orientation for the current processing day.

Contains:

- evaluation model label
- meaningful-reply rule summary
- score scale summary
- latest day score
- coverage metrics
- score-band counts
- ego-state counts
- transaction counts
- escalation counts

### `methodology`

Purpose: human-readable explanation of the rubric.

Contains:

- scope defaults
- inclusion and exclusion rules
- 0-10 score scale
- per-dimension point limits
- score-band thresholds
- TA label meanings
- transaction and escalation label meanings
- explicit non-goals

### `data_dictionary`

Purpose: explain each tab and the meaning of key columns.

Contains:

- tab-level purpose
- column or section definitions
- why each output exists

### `daily_history`

Purpose: main structured daily source of truth.

One row per processed day.

Recommended columns:

- `date`
- `score_scale`
- `average_score`
- `median_score`
- `meaningful_reply_count`
- `strong_reply_count`
- `solid_reply_count`
- `watch_reply_count`
- `eligible_chats_reviewed`
- `chats_with_meaningful_replies`

### `weekly_rollup`

Purpose: rolling 7-day aggregate summary.

Recommended columns:

- `window_start`
- `window_end`
- `score_scale`
- `days_included`
- `meaningful_reply_count`
- `average_score`
- `median_score`
- `strong_count`
- `solid_count`
- `watch_count`

### `all_time_rollup`

Purpose: aggregate summary across all processed days.

Recommended columns:

- `score_scale`
- `days_included`
- `eligible_chats_reviewed`
- `chats_with_meaningful_replies`
- `meaningful_reply_count`
- `average_score`
- `median_score`
- `strong_count`
- `solid_count`
- `watch_count`

### `daily_trend`

Purpose: chart-ready daily scoring trend data.

Recommended columns:

- `date`
- `meaningful_reply_count`
- `average_score`
- `strong_reply_count`
- `solid_reply_count`
- `watch_reply_count`

### `transaction_trend`

Purpose: chart-ready interaction-fit trend data.

Recommended columns:

- `date`
- `complementary`
- `crossed_risk`

### `ego_state_trend`

Purpose: chart-ready ego-state trend data.

Recommended columns:

- `date`
- `Adapted Child`
- `Adult`
- `Nurturing Parent`

## Source Of Truth Guidance

Use `daily_history` as the main day-level source of truth inside the workbook.

Use rollup and trend tabs as derived views.

Use `methodology` and `data_dictionary` to make the workbook interpretable by
someone who did not build the scoring system.

## Scale Clarification

The workbook uses a `0-10` reply-level rubric.

It does not use the older `0-100` weighted daily percentage model.
That distinction should remain explicit in the workbook to avoid confusion.