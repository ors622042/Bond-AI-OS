# Bond AI OS V2.5 - Score Engine
from indicators.risk import risk_score
from data.market import get_etf_price


def etf_score(etf):
    risk, level = risk_score(etf)
    price = get_etf_price(etf)

    score = risk

    action = "HOLD"

    if score > 85:
        action = "ACCUMULATE"
    elif score < 70:
        action = "WATCH"

    return {
        "etf": etf,
        "price": price,
        "score": score,
        "risk_level": level,
        "action": action
    }