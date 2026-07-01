# Bond AI OS V4 - Macro Risk Engine
from data.market import get_credit_spread, get_default_rate
from data.fred import get_fed_funds_rate

def macro_risk_score():
    fed = get_fed_funds_rate()
    default = get_default_rate()
    spread = get_credit_spread()

    score = 100

    if fed > 5:
        score -= (fed - 5) * 8

    score -= default * 800
    score -= spread * 6

    if score >= 80:
        level = "🟢 LOW"
    elif score >= 65:
        level = "🟡 MEDIUM"
    else:
        level = "🔴 HIGH"

    return score, level