"""
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
    Создает случайное изображение заданного размера
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
    page.get_by_role("textbox", name="Название карты").click()
    page.get_by_role("textbox", name="Название карты").fill("лотерея")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#85b78f")
    page.locator("[id=\"__next\"] div").filter(has_text="Выберите цвета вашей карты.Выберите цвет вашей открытки и текста. После того, ка").nth(2).click()
    page.get_by_role("button", name="Продолжить").click()

    page.get_by_role("button", name="Назад").click()
    page.get_by_label("", exact=True).first.click()
    page.get_by_label("", exact=True).first.fill("#07567e")
    page.locator("[id=\"__next\"] div").filter(has_text="Выберите цвета вашей карты.Выберите цвет вашей открытки и текста. После того, ка").nth(2).click()
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

    page.get_by_role("spinbutton", name="Сумма для начисления каждого лотерейного билета").click()
    page.get_by_role("spinbutton", name="Сумма для начисления каждого лотерейного билета").fill("500")
    page.locator("div").filter(has_text=re.compile(r"^Нужен ли Вам номер чека\?$")).locator("div").click()
    page.get_by_role("button", name="Продолжить").click()

    page.locator("label > .absolute").first.click()
    page.locator(".flex > .grid").first.click()
    page.get_by_role("button", name="Delete Icon").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    page.get_by_role("button", name="Delete Icon").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("button", name="Пользовательское").click()
    page.get_by_role("listitem").filter(has_text="Пользовательское").click()
    page.get_by_role("textbox", name="Введите имя").click()
    page.get_by_role("textbox", name="Введите имя").fill("удачная цифра")
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("1")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора Обязательный$")).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("2")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора1 Обязательный$")).get_by_role("button").nth(2).click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("3")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора12 Обязательный$")).get_by_role("button").nth(3).click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("4")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора123 Обязательный$")).get_by_role("button").nth(4).click()
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора1234 Обязательный$")).locator("label div").click()
    page.get_by_role("button", name="Добавить").nth(1).click()
    page.get_by_role("button", name="Продолжить").click()

    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Имя Фамилия").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Количество билетов").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Потрачено").click()
    page.get_by_role("button", name="Продолжить").click()

    page.locator("button:nth-child(2)").first.click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("button", name="Продолжить").click()

    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("textbox", name="скидка 20%").click()
    page.get_by_role("textbox", name="скидка 20%").fill("30")
    page.get_by_role("textbox", name="Введите адрес или место").click()
    page.get_by_role("textbox", name="Введите адрес или место").fill("ю")
    page.get_by_text("Южная Корея").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Завершить").click()

    page.get_by_role("link", name="Перейти к панели управления").click()

    copied_text = page.get_by_role("textbox").filter(has_text=re.compile(r"^$")).input_value()
    print(f"Создана карта лотерея. UUID карты: {copied_text}")

"""

import re
import os
import pytest
import random
import pyperclip
import requests
import pyperclip
from playwright.sync_api import Page, expect
from PIL import Image, ImageDraw

TEMP_IMAGE_FOLDER = "temp_images"  # Папка для временных изображений
os.makedirs(TEMP_IMAGE_FOLDER, exist_ok=True)


def generate_random_image(filename, width, height):
    """Создает случайное изображение заданного размера."""
    img = Image.new(
        "RGB",
        (width, height),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Test Image", fill=(255, 255, 255))
    img_path = os.path.join(TEMP_IMAGE_FOLDER, filename)
    img.save(img_path)
    return img_path


def test_create_stamp(page_with_video, request) -> None:
    page = page_with_video
    # Генерация случайных изображений перед загрузкой
    logo_path = generate_random_image("logo.png", 480, 150)
    banner_path = generate_random_image("banner.png", 1125, 432)
    notification_logo_path = generate_random_image("notification_logo.png", 150, 150)
    stamp_icon_path = generate_random_image("stamp_icon.png", 150, 150)

    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="English").locator("span").nth(2).click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("link", name="Sign in").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("A200200052!")
    page.get_by_role("button", name="Sign in").click()

    page.locator(".p-5 > div > a").click()
    page.get_by_role("button", name="Icon Lottery").click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("Lottery")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#ea8a8a")
    page.locator('[id="__next"] div').filter(
        has_text="Choose your card colors.Pick"
    ).nth(2).click()
    page.get_by_role("button", name="Continue").click()

    page.locator("label").filter(
        has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels"
    ).locator("div").first.click()
    page.locator("label").filter(
        has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels"
    ).locator("input[type='file']").set_input_files(logo_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator(
        "div"
    ).first.click()
    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator(
        "input[type='file']"
    ).set_input_files(banner_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="This will appear as the icon").locator(
        "div"
    ).first.click()
    page.locator("label").filter(has_text="This will appear as the icon").locator(
        "input[type='file']"
    ).set_input_files(notification_logo_path)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("spinbutton", name="The amount to be credited for").click()
    page.get_by_role("spinbutton", name="The amount to be credited for").fill("500")
    page.locator("div").filter(
        has_text=re.compile(r"^Do you need the receipt number\?$")
    ).locator("div").click()
    page.locator("div").filter(
        has_text=re.compile(r"^Do you need the receipt number\?$")
    ).locator("div").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("label > .absolute").first.click()
    page.locator(".flex > .grid").first.click()
    page.get_by_role("button", name="Delete Icon").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Enter name").click()
    page.get_by_role("textbox", name="Enter name").fill("are you happy today?")
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("Yes")
    page.locator("div").filter(
        has_text=re.compile(r"^Field TypeCustomField nameChoice Options Required$")
    ).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("No")
    page.locator("div").filter(
        has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsYes Required$")
    ).get_by_role("button").nth(2).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("I dont know")
    page.locator("div").filter(
        has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsYesNo Required$")
    ).get_by_role("button").nth(3).click()
    page.get_by_role("button", name="Add").nth(1).click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Full Name").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Number of tickets").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Total Spent").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("youtube")
    page.locator("div").filter(has_text=re.compile(r"^common\.selectPlaceholder$")).nth(
        2
    ).click()
    page.get_by_text("Description", exact=True).click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill("YouTube.com")
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="% discount").click()
    page.get_by_role("textbox", name="% discount").fill("50")
    page.get_by_role("textbox", name="Type an address or a place").click()
    page.get_by_role("textbox", name="Type an address or a place").fill("Bali")
    page.get_by_text("Bali Indonesia").click()
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()

    page.get_by_role("link", name="Go to Dashboard").click()

    page.get_by_role("heading", name="Card Lottery").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    page.get_by_role("button").filter(
        has_text=re.compile(r"^$")
    ).click()  # Нажать на кнопку "копировать"
    page.wait_for_timeout(500)  # Подождать, пока скопируется
    copied_text = pyperclip.paste()
    print(f"Создана карта лотерея. UUID карты: {copied_text}")

    request.node.test_info = {"message": f"Создана карта лотерея!\nUUID: {copied_text}"}
