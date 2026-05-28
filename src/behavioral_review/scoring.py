from __future__ import annotations

from dataclasses import dataclass
from statistics import fmean


POSITIVE_THRESHOLD = 1.25
NEGATIVE_THRESHOLD = -0.75
GOOD_DAY_THRESHOLD = 70
WATCH_DAY_THRESHOLD = 45


@dataclass(frozen=True)
class MessageAssessment:
    adult_clarity: int
    collaborative_tone: int
    de_escalation: int
    actionability: int
    respect: int

    def weighted_score(self) -> float:
        weights = {
            "adult_clarity": 0.30,
            "collaborative_tone": 0.20,
            "de_escalation": 0.20,
            "actionability": 0.15,
            "respect": 0.15,
        }
        total = (
            self.adult_clarity * weights["adult_clarity"]
            + self.collaborative_tone * weights["collaborative_tone"]
            + self.de_escalation * weights["de_escalation"]
            + self.actionability * weights["actionability"]
            + self.respect * weights["respect"]
        )
        return round(total, 2)

    def label(self) -> str:
        score = self.weighted_score()
        if score >= POSITIVE_THRESHOLD:
            return "positive_example"
        if score <= NEGATIVE_THRESHOLD:
            return "negative_example"
        return "neutral_example"


def daily_score(assessments: list[MessageAssessment]) -> int:
    if not assessments:
        return 50
    average = fmean(item.weighted_score() for item in assessments)
    normalized = ((average + 3) / 6) * 100
    return max(0, min(100, round(normalized)))


def daily_band(score: int) -> str:
    if score >= GOOD_DAY_THRESHOLD:
        return "good_day"
    if score >= WATCH_DAY_THRESHOLD:
        return "watch_day"
    return "risk_day"


def summarize_day(assessments: list[MessageAssessment]) -> dict[str, int | str]:
    score = daily_score(assessments)
    labels = [item.label() for item in assessments]
    return {
        "daily_score": score,
        "band": daily_band(score),
        "positive_examples": labels.count("positive_example"),
        "negative_examples": labels.count("negative_example"),
        "neutral_examples": labels.count("neutral_example"),
    }
