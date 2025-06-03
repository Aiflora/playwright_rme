from playwright.sync_api import sync_playwright
from screeninfo import get_monitors
import os

# Определяем окружение (по умолчанию 'prod')
ENV = os.getenv("TEST_ENV", "prod")
testDir = "tests/"
trace: True

# Выбираем правильный URL в зависимости от окружения
if ENV == "dev":
    from configs.config_dev import BASE_URL
else:
    from configs.config_prod import BASE_URL

# Функция запуска браузера с нужными параметрами
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Получаем размеры первого доступного монитора
        monitors = get_monitors()
        if not monitors:
            raise RuntimeError("Не удалось определить размеры экрана.")
        monitor = monitors[0]
        width = monitor.width
        height = monitor.height

        # Создаём контекст с динамическим размером экрана
        context = browser.new_context(
            viewport={"width": width, "height": height},
            base_url=BASE_URL,
            record_video_dir="results/videos/",
            record_har_path="results/logs/network.har"
        )

        # Включаем трассировку
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        return context

# Конфигурация Playwright для pytest
def pytest_playwright_config():
    return {
        "browser": "chromium",
        "headless": False,  # Можно изменить на False для тестирования с UI
        "baseURL": BASE_URL
        
    }


