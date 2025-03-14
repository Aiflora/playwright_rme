import re
import os
import pytest
import random
from playwright.sync_api import Page, expect
from PIL import Image, ImageDraw

# Папка для временных изображений
TEMP_IMAGE_FOLDER = "temp_images"
os.makedirs(TEMP_IMAGE_FOLDER, exist_ok=True)

def generate_random_image(filename, width, height):
    """Создает случайное изображение заданного размера."""
    img = Image.new("RGB", (width, height), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Test Image", fill=(255, 255, 255))
    img_path = os.path.join(TEMP_IMAGE_FOLDER, filename)
    img.save(img_path)
    return img_path

def test_example(page: Page) -> None:
    # Генерация случайных изображений перед загрузкой
    logo_path = generate_random_image("logo.png", 480, 150)
    banner_path = generate_random_image("banner.png", 1125, 432)
    notification_logo_path = generate_random_image("notification_logo.png", 150, 150)
    stamp_icon_path = generate_random_image("stamp_icon.png", 150, 150)

    # Открытие сайта
    page.goto("https://www.recardme.com/")
    
    # Выбор русского языка и подтверждение
    page.locator("label").filter(has_text="Русский").locator("span").nth(1).click()
    page.get_by_role("button", name="Подтвердить").click()

    # Переход на страницу входа
    page.locator(".w-full > .flex > .btn").click()
    page.get_by_role("button", name="Войдите в систему с существующей учетной записью").click()

    # Ввод email и пароля
    page.wait_for_selector("#email")
    page.locator("#email").fill("test_prod@gmail.com")

    page.wait_for_selector("#password")
    page.locator("#password").fill("A200200052!")

    # Вход в аккаунт
    page.get_by_role("button", name="Вход").click()

    # Ожидание редиректа после входа (указать реальный URL)
    page.wait_for_url("**/dashboard")

    # Ожидание загрузки кнопки "Загрузить логотип"
    page.wait_for_selector("text=Загрузить логотип", timeout=10000)
    assert page.locator("text=Загрузить логотип").is_visible()
    page.get_by_text("Загрузить логотип").click(force=True)
    page.locator("body").set_input_files(logo_path)

    # Аналогично для остальных загрузок
    page.wait_for_selector("text=Загрузить баннер", timeout=10000)
    assert page.locator("text=Загрузить баннер").is_visible()
    page.get_by_text("Загрузить баннер").click(force=True)
    page.locator("body").set_input_files(banner_path)

    page.wait_for_selector("text=Логотип для уведомлений", timeout=10000)
    assert page.locator("text=Логотип для уведомлений").is_visible()
    page.get_by_text("Логотип для уведомлений").click(force=True)
    page.locator("body").set_input_files(notification_logo_path)

    page.wait_for_selector("text=Загрузить пользовательскую иконку штампа", timeout=10000)
    assert page.locator("text=Загрузить пользовательскую иконку штампа").is_visible()
    page.get_by_text("Загрузить пользовательскую иконку штампа").click(force=True)
    page.locator("body").set_input_files(stamp_icon_path)

    # Переход к следующему шагу
    page.wait_for_selector("text=Продолжить", timeout=10000)
    assert page.locator("text=Продолжить").is_visible()
    page.get_by_role("button", name="Продолжить").click()
