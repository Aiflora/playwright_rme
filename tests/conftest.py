"""
import os
import pytest
import time
import datetime
import requests
from playwright.sync_api import sync_playwright

VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

TELEGRAM_TOKEN = "7606399616:AAH8KmbIV46OZtQYSYy1knVTQYD7J2BiRcU"
CHAT_ID = "-4527522890"  # -1002099866066/11392 - bag report group  -4527522890 -Bugs rme group -1002099866066  https://t.me/c/2099866066/11392

@pytest.fixture(scope="function")
def page_with_video(request):  # добавим request для имени теста
    test_name = request.node.name  # имя теста (например, test_example)
    
    # Новое: имя файла теста (например, test_create_cashback)
    test_file = os.path.basename(request.node.location[0]).replace(".py", "")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_base = f"{test_file}_{timestamp}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=VIDEO_DIR)
        page = context.new_page()

        yield page

        video_path = None
        try:
            video = page.video
            context.close()
            browser.close()
            original_path = video.path()

            # Новое имя файла
            new_filename = f"{filename_base}.webm"
            new_path = os.path.join(VIDEO_DIR, new_filename)
            os.rename(original_path, new_path)  # Переименуем

            video_path = new_path
        except Exception as e:
            print("❌ Ошибка при обработке видео:", e)

        if video_path:
            print(f"📹 Видео готово: {video_path}")
            for i in range(10):
                if os.path.exists(video_path):
                    print("✅ Отправка видео в Telegram.")
                    with open(video_path, "rb") as f:
                        response = requests.post(
                            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo",
                            data={"chat_id": CHAT_ID, "caption": f"🎬 {filename_base}"},
                            files={"video": f}
                        )
                    print("📤 Ответ Telegram:", response.status_code, response.text)
                    break
                else:
                    print(f"⏳ Ожидаем файл... попытка {i+1}")
                    time.sleep(1)
            else:
                print("❌ Видео не появилось после ожидания.")
        else:
            print("❌ Видео не обработано.")
"""
"""
import os
import pytest
import time
import datetime
import requests
from playwright.sync_api import sync_playwright

VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

TELEGRAM_TOKEN = "7606399616:AAH8KmbIV46OZtQYSYy1knVTQYD7J2BiRcU"
CHAT_ID = "-4527522890"  # -1002099866066/11392 - bag report group  -4527522890 -Bugs rme group -1002099866066  https://t.me/c/2099866066/11392


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат теста
    outcome = yield
    result = outcome.get_result()

    # Сохраняем статус в item (request.node)
    if not hasattr(item, "test_info"):
        item.test_info = {}
    if result.when == "call":
        item.test_info["status"] = "passed" if result.passed else "failed"

@pytest.fixture(scope="function")
def page_with_video(request):
    test_name = request.node.name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_base = f"{test_name}_{timestamp}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=VIDEO_DIR)
        page = context.new_page()

        yield page

        video_path = None
        try:
            video = page.video
            context.close()
            browser.close()
            original_path = video.path()

            new_filename = f"{filename_base}.webm"
            new_path = os.path.join(VIDEO_DIR, new_filename)
            os.rename(original_path, new_path)
            video_path = new_path
        except Exception as e:
            print("❌ Ошибка при обработке видео:", e)

        if video_path:
            test_info = getattr(request.node, "test_info", {})
            uuid = test_info.get("uuid", "UUID неизвестен")
            message = test_info.get("message", "")
            status = test_info.get("status", "unknown")

            status_icon = "✅" if status == "passed" else "❌"
            caption = f"{status_icon} [{status.upper()}] {test_name}\n{message}\nUUID: {uuid}"

            print(f"📹 Видео готово: {video_path}")
            for i in range(10):
                if os.path.exists(video_path):
                    print("✅ Отправка видео в Telegram.")
                    with open(video_path, "rb") as f:
                        response = requests.post(
                            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo",
                            data={"chat_id": CHAT_ID, "caption": caption},
                            files={"video": f}
                        )
                    print("📤 Ответ Telegram:", response.status_code, response.text)
                    break
                else:
                    print(f"⏳ Ожидаем файл... попытка {i+1}")
                    time.sleep(1)
            else:
                print("❌ Видео не появилось после ожидания.")
        else:
            print("❌ Видео не обработано.")

            
response = requests.post(
                            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo",
                            data={"chat_id": CHAT_ID, "caption": caption},
                            files={"video": f}

https://api.telegram.org/bot7606399616:AAH8KmbIV46OZtQYSYy1knVTQYD7J2BiRcU/getUpdates узнать chat id                           

"chat": {
            "id": -1002099866066,
            "title": "Recardme Core Team",
            "is_forum": true,
            "type": "supergroup"
          },
          "date": 1730093796,
          "message_thread_id": 11392,
          "forum_topic_created": {
            "name": "Bag reports",
            "icon_color": 16749490
          },
          "is_topic_message": true
        },
        "text": "test",
        "is_topic_message": true                      )

"""
import os
import pytest
import time
import datetime
import requests
from playwright.sync_api import sync_playwright

VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

TELEGRAM_TOKEN = "7606399616:AAH8KmbIV46OZtQYSYy1knVTQYD7J2BiRcU"
CHAT_ID = "-1002099866066/11392"  # -1002099866066/11392 - bag report group HANSE LANDA https://t.me/c/2099866066/1  -4527522890 -Bugs rme group -1002099866066  https://t.me/c/2099866066/11392


# Хук для отслеживания статуса теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if not hasattr(item, "test_info"):
        item.test_info = {}
    if result.when == "call":
        item.test_info["status"] = "passed" if result.passed else "failed"

@pytest.fixture(scope="function")
def page_with_video(request):
    test_name = request.node.name
    test_file = os.path.basename(request.node.location[0]).replace(".py", "")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_base = f"{test_file}_{timestamp}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=VIDEO_DIR)
        page = context.new_page()

        yield page

        video_path = None
        try:
            video = page.video
            context.close()
            browser.close()
            original_path = video.path()

            new_filename = f"{filename_base}.webm"
            new_path = os.path.join(VIDEO_DIR, new_filename)
            os.rename(original_path, new_path)

            video_path = new_path
        except Exception as e:
            print("❌ Ошибка при обработке видео:", e)

        if video_path:
            print(f"📹 Видео готово: {video_path}")

            test_info = getattr(request.node, "test_info", {})
            uuid = test_info.get("uuid", "неизвестен")
            message = test_info.get("message", "")
            status = test_info.get("status", "unknown")
            status_icon = "✅" if status == "passed" else "❌"
            caption = (
                f"{status_icon} {status.upper()} - {test_file}\n"
                f"{message}\nUUID: {uuid}"
            )

            for i in range(10):
                if os.path.exists(video_path):
                    print("✅ Отправка видео в Telegram.")
                    with open(video_path, "rb") as f:
                        response = requests.post(
                            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo",
                        data={
                            "chat_id": CHAT_ID,
                            "message_thread_id": 11392,  # 🎯 указываем нужный раздел группы
                            "caption": caption
                        },
                        files={"video": f}
                        )

                    print("📤 Ответ Telegram:", response.status_code, response.text)
                    break
                else:
                    print(f"⏳ Ожидаем файл... попытка {i+1}")
                    time.sleep(1)
            else:
                print("❌ Видео не появилось после ожидания.")
        else:
            print("❌ Видео не обработано.")
