from config import ETFS
from indicators.score import etf_score
from report.generator import generate_report


def run():
    print("Bond AI OS V5/V6 Auto Report System")
    print("================================")

    results = []

    for etf in ETFS:
        result = etf_score(etf)
        results.append(result)

        print(f"ETF: {result['etf']}")
        print(f"Price: {result['price']}")
        print(f"Score: {result['score']:.2f}")
        print(f"Risk: {result['risk_level']}")
        print(f"Action: {result['action']}")
        print("--------------------------------")

    print("\nGenerating daily report...\n")

    report = generate_report()

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("Report saved: report.md")
    print("Summary complete.")


if __name__ == "__main__":
    run()