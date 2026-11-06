import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate

#Example test cases:
def test_excellent_band():
    assert credit_band(800) == "excellent"

def test_eligible():
    assert is_eligible(30, 50000, "salaried", 800) is True

#Write the rest of the test cases so that the code is 90- 100% covered.
