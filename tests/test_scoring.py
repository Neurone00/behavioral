from behavioral_review.scoring import MessageAssessment, daily_band, daily_score, summarize_day


def test_positive_example_label():
    assessment = MessageAssessment(3, 2, 2, 2, 2)
    assert assessment.label() == 'positive_example'


def test_negative_example_label():
    assessment = MessageAssessment(-2, -2, -2, 0, -2)
    assert assessment.label() == 'negative_example'


def test_daily_score_normalizes():
    assessments = [
        MessageAssessment(3, 2, 2, 2, 2),
        MessageAssessment(2, 2, 1, 2, 2),
    ]
    assert daily_score(assessments) > 70


def test_daily_band_thresholds():
    assert daily_band(75) == 'good_day'
    assert daily_band(50) == 'watch_day'
    assert daily_band(40) == 'risk_day'


def test_summarize_day_counts_examples():
    assessments = [
        MessageAssessment(3, 2, 2, 2, 2),
        MessageAssessment(-2, -2, -2, 0, -2),
        MessageAssessment(1, 0, 0, 1, 0),
    ]
    summary = summarize_day(assessments)
    assert summary['positive_examples'] == 1
    assert summary['negative_examples'] == 1
    assert summary['neutral_examples'] == 1
