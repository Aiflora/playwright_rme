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
    page.get_by_role("button", name="Icon Кешбек карта").click()
    page.get_by_role("textbox", name="Название карты").click()
    page.get_by_role("textbox", name="Название карты").fill("Кешбек")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#6d1c24")
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

    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("textbox", name="Gold").click()
    page.get_by_role("textbox", name="Gold").fill("уровень")
    page.get_by_placeholder("100").click()
    page.get_by_placeholder("100").fill("20000")
    page.get_by_placeholder("5").click()
    page.get_by_placeholder("5").fill("15")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("textbox", name="USD").fill("USD")
    page.get_by_role("button", name="Add", exact=True).click()
    page.get_by_role("button", name="Продолжить").click()
    """
    page.get_by_role("button", name="addDynamicCashback").click()
    page.wait_for_timeout(3000)
    page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5").click()
    page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5").fill("80")
    # page.wait_for_timeout(3000)
    # page.get_by_role("heading", name="Процент %").nth(1).click()
    # page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5").click()
    # page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5").click()
    # page.wait_for_selector("input[placeholder='5']", timeout=5000)
    # page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5").fill("1")
    # locator = page.locator("div").filter(has_text=re.compile(r"^Процент %startTimeendTimeupdateDynamicCashback$")).get_by_placeholder("5")
    # locator.wait_for(state="visible", timeout=30000)
    # locator.fill("1")
    # page.locator("input[name=\"start_time\"]").click()
    page.locator("input[name=\"start_time\"]").click()
    page.locator("input[name=\"start_time\"]").fill("09:00")
    page.locator("input[name=\"end_time\"]").click()
    page.locator("input[name=\"end_time\"]").fill("18:00")
    page.get_by_role("button", name="Edit").click()"
    
    """
    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("button", name="Пользовательское").click()
    page.get_by_role("listitem").filter(has_text="Пользовательское").click()
    page.get_by_role("textbox", name="Введите имя").click()
    page.get_by_role("textbox", name="Введите имя").fill("любимый напиток")
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("чай")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выбора Обязательный$")).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("кофе")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выборачай Обязательный$")).get_by_role("button").nth(2).click()
    page.get_by_role("textbox", name="Введите название выбора").click()
    page.get_by_role("textbox", name="Введите название выбора").fill("вода")
    page.locator("div").filter(has_text=re.compile(r"^Тип поляПользовательскоеНаименование поляВарианты выборачайкофе Обязательный$")).get_by_role("button").nth(3).click()
    page.get_by_role("button", name="Добавить").nth(1).click()
    page.locator("div:nth-child(5) > .flex > .relative > .absolute").click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Имя Фамилия").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Уровень").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Баланс").click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("заголовок")
    page.locator("div").filter(has_text=re.compile(r"^\.\.\.$")).nth(2).click()
    page.get_by_text("Description").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill("123")
    page.locator("button").filter(has_text=re.compile(r"^Добавить$")).click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_role("textbox", name="скидка 20%").click()
    page.get_by_role("textbox", name="скидка 20%").fill("20")
    page.get_by_role("textbox", name="Введите адрес или место").click()
    page.get_by_role("textbox", name="Введите адрес или место").fill("Бишкек")
    page.get_by_role("listitem").filter(has_text="Бишкек шаары Kyrgyzstan").locator("small").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Завершить").click()
    page.get_by_role("link", name="Перейти к панели управления").click()

    copied_text = page.get_by_role("textbox").filter(has_text=re.compile(r"^$")).input_value()
    print(f"Создана карта подписка. UUID карты: {copied_text}")