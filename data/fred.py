# Bond AI OS V4 - FRED Data Layer (Real API Ready)
# You can add your FRED API KEY later

import requests

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

API_KEY = None  # optional: set your FRED API key


def get_fed_funds_rate():
    # fallback mock if no API key
    if not API_KEY:
        return 5.25

    params = {
        "series_id": "FEDFUNDS",
        "api_key": API_KEY,
        "file_type": "json"
    }
    r = requests.get(FRED_BASE, params=params, timeout=10)
    data = r.json()

    return float(data["observations"][-1]["value"])
