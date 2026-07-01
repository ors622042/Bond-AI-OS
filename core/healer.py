# Bond AI OS V11 - Self-Healing Engine
# Responsible for detecting failures and triggering recovery strategies

from core.self_test import run_self_test

class SystemHealer:
    def __init__(self):
        self.last_health = None

    def diagnose(self):
        report = run_self_test()
        self.last_health = report
        return report

    def needs_healing(self, report):
        if report["health_score"] < 80:
            return True
        for k, v in report["results"].items():
            if v[0] is False:
                return True
        return False

    def heal(self, report):
        actions = []
        if not report["results"]["data"][0]:
            actions.append("SWITCH_TO_FALLBACK_DATA")
        if not report["results"]["engine"][0]:
            actions.append("REDUCE_ENGINE_COMPLEXITY")
        if report["health_score"] < 60:
            actions.append("RULES_ONLY_MODE")
        return {
            "healing_actions": actions,
            "status": "RECOVERY_MODE" if actions else "OK"
        }