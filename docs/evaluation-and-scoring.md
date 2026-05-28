# Evaluation And Scoring

This document describes the active behavioral review rubric used for the daily
Teams communication review.

## Purpose

The system is designed to review professional communication quality, not
personality. It uses Transactional Analysis as a lightweight interpretive frame
for work interactions.

All classifications are evidence-based hypotheses drawn from message text.
They are not diagnoses, personality claims, or therapeutic judgments.

## Scope

Default scope:

- one day at a time only
- timezone: `Europe/Rome`
- time window: `00:00` local time through time of execution
- 1:1 and group chats first
- meeting chats excluded
- channel chats excluded by default
- bot and system messages excluded
- no historical backfill by default

Only the user's meaningful replies are scored.

## Meaningful Reply Rule

A meaningful reply is a Luca-authored message that materially advances the work
or meaning of the conversation.

Typical qualifying behaviors:

- clarifies ambiguity
- states a constraint or fact
- proposes a next step
- makes or narrows a decision
- repairs tone or reassures when context calls for it
- answers a question in a way that improves shared understanding

Typical non-qualifying messages:

- greetings only
- acknowledgements with no substance
- filler replies
- image-only posts
- system-generated content

## Deterministic Reply Rubric

Each scored reply receives a total from `0` to `10`.

| Key | Max | Interpretation |
| --- | ---: | --- |
| `adult_clarity` | 3 | Specific, reality-based communication that clarifies facts, limits, or uncertainty |
| `transaction_fit` | 2 | Reply stays aligned with the incoming work transaction instead of crossing it unnecessarily |
| `tone_regulation` | 2 | Tone reduces friction and avoids avoidable escalation |
| `actionability` | 2 | Reply helps the other person decide, act, or move the task forward |
| `repair_or_empathy` | 1 | Useful relational repair, acknowledgement, or reassurance when context makes it relevant |

Total score formula:

`adult_clarity + transaction_fit + tone_regulation + actionability + repair_or_empathy`

Daily score formula:

`average(overall_score for all meaningful replies in the day)`

## Score Bands

| Band | Range | Reading |
| --- | --- | --- |
| `strong` | `8.00-10.00` | Clear Adult communication with strong practical value |
| `solid` | `5.00-7.99` | Workable and often useful, but not consistently strong across all dimensions |
| `watch` | `0.00-4.99` | Greater risk of friction, ambiguity, or crossed-transaction effects |

## TA Labels

These labels describe the visible communication stance of a reply, not the
person as a whole.

| Label | Working definition |
| --- | --- |
| `Adult` | factual, bounded, practical, problem-solving |
| `Nurturing Parent` | supportive, reassuring, calming, pressure-reducing |
| `Adapted Child` | defensive, avoidant, appeasing, or narrowly reactive |

## Transaction And Escalation Labels

Transaction type:

- `complementary`: reply fits the incoming work interaction and helps the exchange continue productively
- `crossed_risk`: reply introduces a mismatch that may increase misunderstanding or defensiveness

Escalation effect:

- `de-escalating`: likely lowers tension or restores workability
- `stable`: unlikely to materially change tension
- `mild_risk`: may raise tension or friction if received poorly

## What The System Does Not Do

The system does not:

- infer personality traits
- diagnose
- assign clinical meaning
- claim hidden motives as facts
- treat TA labels as identity labels

## Reporting Guidance

GitHub should store only safe structured outputs, code, prompts, schemas, and
operational artifacts.

Private locations outside GitHub should hold:

- raw Teams JSON
- raw message text
- narrative reports with sensitive detail

## Suggested Review Questions

When interpreting any score, the safest questions are:

- Was the reply clear?
- Did it fit the incoming work transaction?
- Did it reduce or increase friction?
- Did it move the work forward?
- Did it add repair or acknowledgement when needed?