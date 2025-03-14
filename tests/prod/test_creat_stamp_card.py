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

    # Открытие сайта и вход
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="English").locator("span").nth(2).click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("link", name="Sign in").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("A200200052!")
    page.get_by_role("button", name="Sign in").click()

    # Ожидание редиректа после входа (указать реальный URL) Ждем, пока загрузится страница после входа

    page.get_by_role("link").filter(has_text=re.compile(r"^$")).nth(1).click()
    page.get_by_role("button", name="Icon Member").click()
    page.get_by_role("button", name="Icon Stamp", exact=True).click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("stamp")
    page.get_by_role("button", name="Recard Me").click()
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#9c8dd3")
    page.locator("[id=\"__next\"] div").filter(has_text="Choose your card colors.Pick").nth(2).click()
    page.get_by_role("button", name="Continue").click()


    # Ожидание загрузки кнопки "Загрузить логотип"
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("input[type='file']").set_input_files(logo_path)

    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator("input[type='file']").set_input_files(banner_path)

    page.locator("label div").first.click()
    page.locator("label div").locator("input[type='file']").set_input_files(notification_logo_path, timeout=60000)


    page.get_by_role("button", name="Continue").click()

    page.locator("label div").nth(1).click()
    page.locator("label div").locator("input[type='file']").set_input_files(stamp_icon_path)

    page.get_by_role("button", name="Continue").click()

