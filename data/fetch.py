# Bond AI OS V10 - Data Fetch Layer
# Only responsible for fetching raw data

import requests


def get_etf_price(etf: str):
    # Placeholder safe mock (replace with real API later)
    return 100.0


def get_macro_data():
    # Stable fallback macro snapshot
    return {
        "fed_rate": 5.25,
        "credit_spread": 2.1,
        "default_rate": 0.02
    }