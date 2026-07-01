# Bond AI OS V6 - Report Generator
from datetime import datetime
from indicators.score import etf_score
from config import ETFS


def generate_report():
    lines = []
    lines.append("# 📊 Bond AI OS Daily Report")
    lines.append(f"Generated: {datetime.now()}")
    lines.append("\n---\n")

    for etf in ETFS:
        r = etf_score(etf)

        lines.append(f"## {r['etf']}")
        lines.append(f"- Price: {r['price']}")
        lines.append(f"- Score: {r['score']:.2f}")
        lines.append(f"- Risk: {r['risk_level']}")
        lines.append(f"- Action: **{r['action']}**")
        lines.append("\n")

    return "\n".join(lines)
