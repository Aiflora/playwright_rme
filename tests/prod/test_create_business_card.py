import re
import os
import pytest
import random
import pyperclip
import time
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
    logo_path = generate_random_image("logo.png", 128, 128)

    # Открытие сайта и вход
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="Русский").locator("span").nth(1).click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("link", name="Вход").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("A200200052!")
    page.get_by_role("button", name="Вход").click()

    page.locator(".p-5 > div > a").click()
    page.get_by_role("button", name="Icon Лотерея").click()
    page.get_by_role("button", name="Icon Бизнес").click()
    page.get_by_role("textbox", name="Название карты").click()
    page.get_by_role("textbox", name="Название карты").fill("Бизнес")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#3b3357")
    page.get_by_text("Цвет текстаЦвет заднего фона").click()
    page.get_by_role("button", name="Продолжить").click()

    page.locator("label").filter(has_text="Рекомендуемые размеры:Прямоугольный: 480 x 150 пикселейКвадрат: 150 x 150").locator("div").first.click()
    page.locator("label").filter(has_text="Рекомендуемые размеры:Прямоугольный: 480 x 150 пикселейКвадрат: 150 x 150").locator("input[type='file']").set_input_files(logo_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="Рекомендуемые размеры:1125 x").locator("div").first.click()
    page.locator("label").filter(has_text="Рекомендуемые размеры:1125 x").locator("input[type='file']").set_input_files(banner_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="Это будет отображаться в виде значка на экранах блокировки пользователей, когда").locator("div").first.click()
    page.locator("label").filter(has_text="Это будет отображаться в виде значка на экранах блокировки пользователей, когда").locator("input[type='file']").set_input_files(notification_logo_path)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Продолжить").click()

    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Продолжить").click()

    page.get_by_role("button", name="Empty").first.click()
    page.locator("div").filter(has_text=re.compile(r"^EmptyПустоПользовательское$")).get_by_role("button").click()
    page.get_by_role("button", name="Продолжить").click()

    # page.get_by_text("Загрузить логотип").click()
    # page.locator("label div").first.click().filter("body").set_input_files(logo_path)
    page.locator("label div").first.click()
    page.locator("input[type='file']").set_input_files(logo_path, timeout=5000)
    # page.locator("body").set_input_files(logo_path)
    # page.locator("body").set_input_files(logo_path)
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Full name").click()
    page.get_by_role("textbox", name="Full name").fill("Recardme core team")
    page.locator(".ql-editor").first.click()
    page.get_by_role("button", name="bold").click()
    page.get_by_role("paragraph").nth(1).click()
    page.locator(".ql-editor").first.fill("aaaaaaaaa ")
    page.get_by_role("button", name="italic").click()
    page.locator(".ql-editor").first.fill("aaaaaaaaa bbbbbb ")
    page.get_by_role("button", name="underline").click()
    page.locator(".ql-editor").first.fill("aaaaaaaaa bbbbbb ccccccc ")
    # page.locator("div").filter(has_text=re.compile(r"^Загрузить логотипСброситьaaaaaaaaa bbbbbb ccccccc$")).get_by_role("paragraph").click()
    page.locator(".ql-editor").first.fill("aaaaaaaaa bbbbbb ccccccc  dddddddd ")
    page.get_by_role("paragraph").nth(1).click()
    page.get_by_role("button", name="blockquote").click()
    page.get_by_role("blockquote").first.click()
    page.get_by_role("button", name="image").click()
    # page.locator(".ql-editor").locator("input[type='file']").set_input_files(logo_path, timeout=5000)
    # page.locator(".ql-editor input[type='file']").wait_for(timeout=10000)
    # page.locator(".ql-editor input[type='file']").set_input_files(logo_path)
    # page.wait_for_selector(".ql-editor input[type='file']", state="visible", timeout=10000)
    # page.locator(".ql-editor input[type='file']").set_input_files(logo_path)
    # frame = page.frame_locator("iframe_selector")  # Замените на правильный селектор
    # frame.locator("input[type='file']").set_input_files(logo_path)


    page.get_by_role("textbox", name="Full name").click()
    page.get_by_role("textbox", name="Full name").fill("Recardme core team =)")
    page.get_by_role("textbox", name="Full name").click()
    page.get_by_role("button", name="Продолжить").click()

    page.locator("div:nth-child(2) > div:nth-child(2) > button:nth-child(2)").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("button", name="Завершить").click()

    page.get_by_role("link", name="Перейти к панели управления").click()

    copied_text = page.get_by_role("textbox").filter(has_text=re.compile(r"^$")).input_value()
    print(f"Создана бизнес карта. UUID карты: {copied_text}")
