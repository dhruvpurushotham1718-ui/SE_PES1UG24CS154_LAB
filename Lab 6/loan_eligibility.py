MIN_INCOME = {"salaried": 25000, "self_employed": 40000}


def credit_band(score):
    if score < 300 or score > 900:
        raise ValueError("invalid score")
    if score >= 750:
        return "excellent"
    elif score >= 650:
        return "good"
    elif score >= 550:
        return "fair"
    return "poor"


def is_eligible(age, income, employment, score):
    if employment not in MIN_INCOME:
        raise ValueError("unknown employment")
    if age < 21 or age > 60:
        return False
    if income < MIN_INCOME[employment]:
        return False
    if credit_band(score) == "poor":
        return False
    return True


def interest_rate(score, employment, has_collateral):
    band = credit_band(score)
    if band == "excellent":
        rate = 8
    elif band == "good":
        rate = 10
    else:
        rate = 13
    if employment == "self_employed":
        rate += 1
    if has_collateral:
        rate -= 2
    return rate
