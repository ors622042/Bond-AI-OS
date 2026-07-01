from config import ETFS
from indicators.score import etf_score


def run():
    print("Bond AI OS V2.5 Starting...")
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

    print("Summary complete.")


if __name__ == "__main__":
    run()