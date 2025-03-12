from playwright.sync_api import sync_playwright
import os

# Определяем окружение (по умолчанию 'prod')
ENV = os.getenv("TEST_ENV", "prod")

# Выбираем правильный URL в зависимости от окружения
if ENV == "dev":
    from configs.config_dev import BASE_URL
else:
    from configs.config_prod import BASE_URL

# Функция запуска браузера с нужными параметрами
def run():
    with sync_playwright() as p:  # Используем контекстный менеджер для управления ресурсами
        browser = p.chromium.launch(headless=False)  # Запуск браузера с UI
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},  # Размер окна
            base_url=BASE_URL,  # Подключаем URL
            record_video_dir="results/videos/",  # Сохраняем видео тестов
            record_har_path="results/logs/network.har"  # Логируем сетевые запросы
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трассировку
        return context

# Конфигурация Playwright для pytest
def pytest_playwright_config():
    return {
        "browser": "chromium",
        "headless": False,  # Можно изменить на False для тестирования с UI
        "baseURL": BASE_URL
    }
