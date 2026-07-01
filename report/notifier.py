# Bond AI OS V8 - Notification System
# Supports Telegram / LINE (webhook placeholder)

import requests
from datetime import datetime

# =========================
# CONFIG (set your keys)
# =========================
TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None
LINE_WEBHOOK_URL = None

# =========================
# Telegram Notification
# =========================

def send_telegram(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[Telegram] Missing config, skip send")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

# =========================
# LINE Notification (Webhook)
# =========================

def send_line(message: str):
    if not LINE_WEBHOOK_URL:
        print("[LINE] Missing webhook, skip send")
        return

    payload = {
        "message": message
    }

    requests.post(LINE_WEBHOOK_URL, json=payload)

# =========================
# Main notify function
# =========================

def notify_all(report_text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    full_message = f"""
📊 Bond AI OS V8 Report
Time: {timestamp}

{report_text}
"""

    print(full_message)

    send_telegram(full_message)
    send_line(full_message)

    return True
