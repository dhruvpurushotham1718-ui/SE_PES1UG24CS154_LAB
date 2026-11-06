import pytest

from loan_eligibility import credit_band, is_eligible, interest_rate


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (300, "poor"),
        (549, "poor"),
        (550, "fair"),
        (649, "fair"),
        (650, "good"),
        (749, "good"),
        (750, "excellent"),
        (900, "excellent"),
    ],
)
def test_credit_band_boundaries_and_decision_branches(score, expected):
    assert credit_band(score) == expected


@pytest.mark.parametrize("score", [299, 901])
def test_credit_band_invalid_score_branches(score):
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(score)


def test_is_eligible_unknown_employment_branch():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "freelancer", 800)


@pytest.mark.parametrize(
    ("age", "expected"),
    [
        (20, False),  # age < 21
        (21, True),   # lower valid boundary
        (60, True),   # upper valid boundary
        (61, False),  # age > 60
    ],
)
def test_is_eligible_age_branches(age, expected):
    assert is_eligible(age, 50000, "salaried", 800) is expected


@pytest.mark.parametrize(
    ("employment", "income", "expected"),
    [
        ("salaried", 24999, False),
        ("salaried", 25000, True),
        ("self_employed", 39999, False),
        ("self_employed", 40000, True),
    ],
)
def test_is_eligible_income_branches(employment, income, expected):
    assert is_eligible(30, income, employment, 800) is expected


def test_is_eligible_poor_and_non_poor_credit_branches():
    assert is_eligible(30, 50000, "salaried", 549) is False
    assert is_eligible(30, 50000, "salaried", 550) is True


@pytest.mark.parametrize(
    ("score", "employment", "has_collateral", "expected"),
    [
        (750, "salaried", False, 8),          # excellent branch
        (650, "salaried", False, 10),         # good branch
        (550, "salaried", False, 13),         # fallback branch
        (750, "self_employed", False, 9),     # employment adjustment
        (750, "salaried", True, 6),           # collateral adjustment
        (750, "self_employed", True, 7),      # both adjustments
    ],
)
def test_interest_rate_decision_and_adjustment_branches(
    score, employment, has_collateral, expected
):
    assert interest_rate(score, employment, has_collateral) == expected
