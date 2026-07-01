# Bond AI OS V2.5 - Risk Engine
from data.market import get_fed_rate, get_default_rate, get_credit_spread


def risk_score(etf):
    base = 100

    fed = get_fed_rate()
    default = get_default_rate()
    spread = get_credit_spread()

    # interest rate risk
    base -= max(0, fed - 3) * 5

    # default risk impact
    base -= default * 1000

    # credit spread impact
    base -= spread * 5

    if base > 85:
        level = "🟢 LOW"
    elif base > 70:
        level = "🟡 MEDIUM"
    else:
        level = "🔴 HIGH"

    return base, level
