# Bond AI OS V5 - AI Decision Engine
from indicators.score import etf_score
from indicators.macro_risk import macro_risk_score


def decide(etf):
    score_data = etf_score(etf)
    macro_score, macro_level = macro_risk_score()

    score = score_data["score"]

    # decision logic V5
    if score >= 85 and macro_level == "🟢 LOW":
        action = "ACCUMULATE"
    elif score >= 80 and macro_level in ["🟢 LOW", "🟡 MEDIUM"]:
        action = "HOLD"
    elif score < 75 or macro_level == "🔴 HIGH":
        action = "WATCH"
    else:
        action = "HOLD"

    return {
        "etf": etf,
        "score": score,
        "macro_level": macro_level,
        "action": action
    }