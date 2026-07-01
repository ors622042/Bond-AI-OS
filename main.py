from config import ETFS


def run():
    print("Bond AI OS V2 Starting...")
    print("Monitoring ETFs:", ETFS)

    for etf in ETFS:
        print(f"Analyzing {etf}...")
        print("Signal: HOLD (default)")


if __name__ == "__main__":
    run()
