# Bond AI OS V10 - Single Entry Point

from config import ETFS
from core.engine import run_engine
from report.generator import generate_report


def main():
    print("🚀 Bond AI OS V10 Stable System Running")
    print("=====================================")

    results = []

    for etf in ETFS:
        result = run_engine(etf)
        results.append(result)

        print(f"ETF: {result['etf']}")
        print(f"Score: {result['score']}")
        print(f"Macro: {result['macro_level']}")
        print(f"Action: {result['action']}")
        print("----------------------------")

    print("\nGenerating report...")
    report = generate_report()

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("Report generated: report.md")


if __name__ == "__main__":
    main()