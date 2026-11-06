import pytest

from loan_eligibility import credit_band, is_eligible, interest_rate


def test_credit_band_returns_each_band():
    assert credit_band(800) == "excellent"
    assert credit_band(700) == "good"
    assert credit_band(600) == "fair"
    assert credit_band(500) == "poor"


def test_credit_band_rejects_scores_below_and_above_range():
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(299)
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(901)


def test_is_eligible_rejects_unknown_employment():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "contract", 800)


def test_is_eligible_rejects_age_outside_range():
    assert is_eligible(20, 50000, "salaried", 800) is False
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_is_eligible_rejects_income_below_minimum():
    assert is_eligible(30, 24999, "salaried", 800) is False
    assert is_eligible(30, 39999, "self_employed", 800) is False


def test_is_eligible_rejects_poor_credit_band():
    assert is_eligible(30, 50000, "salaried", 500) is False


def test_is_eligible_accepts_valid_applications():
    assert is_eligible(30, 25000, "salaried", 650) is True
    assert is_eligible(45, 40000, "self_employed", 750) is True


def test_interest_rate_for_each_credit_band():
    assert interest_rate(800, "salaried", False) == 8
    assert interest_rate(700, "salaried", False) == 10
    assert interest_rate(600, "salaried", False) == 13


def test_interest_rate_adjustments_for_employment_and_collateral():
    assert interest_rate(800, "self_employed", False) == 9
    assert interest_rate(800, "salaried", True) == 6
    assert interest_rate(800, "self_employed", True) == 7
