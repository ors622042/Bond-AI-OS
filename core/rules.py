# Bond AI OS V10 - Rules Engine (Stable Core)

# This layer must NEVER depend on external APIs
# Pure deterministic decision rules only


def decision_rules(score: float, macro_level: str) -> str:
    """
    Stable rule engine for investment decision.
    No AI, no randomness, fully deterministic.
    """

    if score >= 85 and macro_level == "LOW":
        return "ACCUMULATE"

    if score >= 80 and macro_level in ["LOW", "MEDIUM"]:
        return "HOLD"

    if score < 75 or macro_level == "HIGH":
        return "WATCH"

    return "HOLD"
