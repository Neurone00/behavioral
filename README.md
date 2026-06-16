# Behavioral Review Bootstrap

This repository bootstraps a Microsoft Teams behavioral review system using a
Transactional Analysis framing for professional communication.

## Canonical Configuration

The canonical machine-readable scoring and scope definition lives in:

- `config/review-profiles/ta-daily-review-v1.json`

Automation should read that file as the source of truth for scope defaults,
rubric dimensions, score bands, and label definitions.

## What Is Evaluated

The current implementation evaluates only the user's meaningful replies inside
the current day's eligible Teams conversations.

A meaningful reply is a Luca-authored message that materially does at least one
of the following:

- clarifies facts, constraints, or ambiguity
- moves the work forward with a decision, proposal, or next step
- repairs tone or reduces friction when that is contextually useful
- answers a question in a way that advances understanding

By default the system excludes:

- bots and system messages
- greetings-only, filler, or image-only posts
- meeting chats
- channel messages
- historical backfill

Default processing window: `00:00 Europe/Rome` through time of execution on the
same day.

## Current Scoring Model

The active rubric is deterministic and code-friendly. Each meaningful reply is
scored on a `0-10` scale by summing five dimensions.

| Dimension | Max points | What it measures |
| --- | ---: | --- |
| `adult_clarity` | 3 | Specific, reality-based communication that clarifies facts or constraints |
| `transaction_fit` | 2 | Whether the reply stays complementary to the incoming work transaction |
| `tone_regulation` | 2 | Whether the tone reduces friction and avoids avoidable escalation |
| `actionability` | 2 | Whether the reply helps the other person decide, act, or move the task forward |
| `repair_or_empathy` | 1 | Useful relational repair, reassurance, or acknowledgement when context calls for it |

Daily score = average of all scored reply totals for that day.

## Score Bands

- `strong`: `8.00-10.00`
- `solid`: `5.00-7.99`
- `watch`: `0.00-4.99`

These are quality bands for professional communication, not personality labels.

## TA Interpretation Rules

The system uses TA labels as evidence-based hypotheses drawn from the message
text.

- `Adult`: factual, bounded, practical, problem-solving
- `Nurturing Parent`: supportive, reassuring, pressure-reducing, or repairing
- `Adapted Child`: defensive, avoidant, appeasing, or narrowly reactive

It also tracks:

- transaction type: `complementary` or `crossed_risk`
- escalation effect: `de-escalating`, `stable`, or `mild_risk`

The system does not analyze personality, diagnose, or use therapeutic framing.

## Spreadsheet Outputs

The Google Sheets workbook is intended to expose both the data and the scoring
logic clearly.

- `dashboard`: current-day summary and quick orientation
- `methodology`: human-readable scoring criteria and TA interpretation rules
- `data_dictionary`: tab and column explanations
- `daily_history`: one row per processed day
- `weekly_rollup`: rolling 7-day aggregate
- `all_time_rollup`: lifetime aggregate
- `daily_trend`, `transaction_trend`, `ego_state_trend`: chart-ready trend tables

## More Detail

- See `docs/evaluation-and-scoring.md` for the full rubric and interpretation rules.
- See `docs/spreadsheet-data-model.md` for the workbook layout and output structure.

## Privacy

- Raw Teams messages do not belong in GitHub.
- Full narrative reports must stay in approved private storage.
- GitHub should contain only code, prompts, workflows, schemas, and safe structured outputs.