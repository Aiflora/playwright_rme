import pytest
import os

# Создаем папки, если их нет
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    log_dir = "results/logs"
    ensure_directory_exists(log_dir)  # Проверяем перед созданием

    config.option.log_file = os.path.join(log_dir, "test_log.log")
    config.option.log_file_level = "INFO"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")  # Проверяем, есть ли объект страницы
        if page:
            ensure_directory_exists("results/screenshots")
            page.screenshot(path=f"results/screenshots/{item.name}.png")
