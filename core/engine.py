# Bond AI OS V10 - Compute Engine (Deterministic Core)

from indicators.score import etf_score
from indicators.macro_risk import macro_risk_score
from core.rules import decision_rules


def run_engine(etf: str):
    """
    Pure computation layer.
    No API calls, no side effects.
    """

    score_data = etf_score(etf)
    macro_score, macro_level = macro_risk_score()

    score = score_data["score"]

    action = decision_rules(score, macro_level)

    return {
        "etf": etf,
        "score": score,
        "macro_level": macro_level,
        "action": action
    }