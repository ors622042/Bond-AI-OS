# Bond AI OS V10 - Fallback Layer
# Ensures system never breaks when APIs fail

FALLBACK_DATA = {
    "ETFS": {
        "00679B": {"price": 100},
        "00740B": {"price": 100},
        "00945B": {"price": 100},
    },
    "macro": {
        "fed_rate": 5.0,
        "credit_spread": 2.0,
        "default_rate": 0.02,
    }
}

def get_fallback_etf(etf: str):
    return FALLBACK_DATA["ETFS"].get(etf, {"price": 100})


def get_fallback_macro():
    return FALLBACK_DATA["macro"]