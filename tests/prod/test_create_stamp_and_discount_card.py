import re
import os
import pytest
import random
import time
import pyperclip
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

    page.locator(".p-5 > div > a").click()
    page.get_by_role("button", name="Icon Stamp and Discount").click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("stamp and discount")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#09ecd2")
    page.locator("[id=\"__next\"] div").filter(has_text="Choose your card colors.Pick").nth(2).click()
    page.get_by_role("button", name="Continue").click()

    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("input[type='file']").set_input_files(logo_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:1125 x").locator("input[type='file']").set_input_files(banner_path)
    page.wait_for_timeout(1000)
    page.locator("label").filter(has_text="This will appear as the icon").locator("div").first.click()
    page.locator("label").filter(has_text="This will appear as the icon").locator("input[type='file']").set_input_files(notification_logo_path)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Pizza").click()
    page.get_by_role("listitem").filter(has_text="Bicycle").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("div").filter(has_text=re.compile(r"^Gold1000010%RUB$")).get_by_role("button").nth(1).click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    page.get_by_role("textbox", name="Gold").click()
    page.get_by_role("textbox", name="Gold").fill("beginer")
    page.get_by_placeholder("5").click()
    page.get_by_placeholder("5").fill("5")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("textbox", name="USD").fill("KGS")
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("textbox", name="Gold").click()
    page.get_by_role("textbox", name="Gold").fill("Middle")
    page.get_by_placeholder("5").click()
    page.get_by_placeholder("5").fill("10")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("textbox", name="USD").fill("KGS")
    page.get_by_placeholder("100").click()
    page.get_by_placeholder("100").fill("10000")
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="15").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Custom").click()
    page.get_by_text("Gender").click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("F")
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice Options Required$")).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("M")
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsF Required$")).get_by_role("button").nth(2).click()
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsFM Required$")).locator("label div").click()
    page.get_by_role("button", name="Add").nth(1).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Full Name").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Birthday", exact=True).click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Tier").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("button:nth-child(2)").first.click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()

    page.get_by_role("link", name="Go to Dashboard").click()

    copied_text = page.get_by_role("textbox").filter(has_text=re.compile(r"^$")).input_value()
    print(f"Создана карта штампы и скидка. UUID карты: {copied_text}")