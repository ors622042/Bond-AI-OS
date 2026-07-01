# Bond AI OS V2.5 - Market Data (Mock Layer)

ETFS = ["00679B", "00740B", "00945B"]


def get_etf_price(etf):
    mock_prices = {
        "00679B": 31.25,
        "00740B": 38.98,
        "00945B": 14.54,
    }
    return mock_prices.get(etf, 0)


def get_fed_rate():
    return 5.25  # mock


def get_default_rate():
    return 0.03  # 3%


def get_credit_spread():
    return 1.2  # %
