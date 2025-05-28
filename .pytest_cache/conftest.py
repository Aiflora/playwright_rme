
import os
import pytest
import uuid
from playwright.sync_api import sync_playwright
import requests

VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

TELEGRAM_TOKEN = "https://t.me/c/2099866066/1"
CHAT_ID = "https://t.me/c/2099866066/11392"

@pytest.fixture(scope="function")
def page_with_video():
    video_name = f"{uuid.uuid4()}.webm"
    video_path = os.path.join(VIDEO_DIR, video_name)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(record_video_dir=VIDEO_DIR)
        page = context.new_page()

        yield page

        context.close()
        browser.close()

        # Отправка видео в Telegram
        full_video_path = os.path.join(VIDEO_DIR, video_name)
        if os.path.exists(full_video_path):
            with open(full_video_path, "rb") as video_file:
                requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo",
                    data={"chat_id": CHAT_ID},
                    files={"video": video_file}
                )