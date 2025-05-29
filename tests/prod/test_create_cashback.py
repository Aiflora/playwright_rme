import re
import os
import pytest
import random
import pyperclip
import requests
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

def test_example(page_with_video, request) -> None:
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
    page.locator("#email").fill("Aigerimkalil9@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("AinuskaAigerimforever")
    page.get_by_role("button", name="Sign in").click()

    page.locator(".p-5 > div > a").click()
    page.get_by_role("button", name="Icon Cashback").click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("Cashback")
    page.get_by_role("button", name="Recard Me").click()
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#20ac22")
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

    page.get_by_role("button", name="Add").click()
    page.get_by_role("heading", name="Tier Name").click()
    page.get_by_role("textbox", name="Gold").click()
    page.get_by_role("textbox", name="Gold").fill("Diamond")
    page.get_by_placeholder("100").click()
    page.get_by_placeholder("100").fill("20000")
    page.get_by_placeholder("5").click()
    page.get_by_placeholder("5").fill("50")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("textbox", name="USD").fill("USD")
    page.locator("form").get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("div").filter(has_text=re.compile(r"^E-mail$")).first.click()
    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Enter name").click()
    page.get_by_role("textbox", name="Enter name").fill("feelings")
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("Happy")
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice Options Required$")).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("Sad")
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsHappy Required$")).get_by_role("button").nth(2).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("Angry")
    page.locator("div").filter(has_text=re.compile(r"^Field TypeCustomField nameChoice OptionsHappySad Required$")).get_by_role("button").nth(3).click()
    page.get_by_role("button", name="Add").nth(1).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Full Name").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Tier").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Balance").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("instagram")
    page.get_by_text("common.selectPlaceholder").click()
    page.get_by_text("Description", exact=True).click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill("i")
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill("https://www.instagram.com/?hl=en")
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="% discount").click()
    page.get_by_role("textbox", name="% discount").fill("Bishkek")
    page.get_by_role("textbox", name="Type an address or a place").click()
    page.get_by_role("textbox", name="% discount").click()
    page.get_by_role("textbox", name="% discount").fill("here we are")
    page.get_by_role("textbox", name="Type an address or a place").click()
    page.get_by_role("textbox", name="Type an address or a place").fill("Bishkek")
    page.get_by_text("Bishkek Kyrgyzstan").click()
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()
    dashboard_link = page.get_by_role("link", name="Go to Dashboard")
    dashboard_link.wait_for(state="visible", timeout=60000)
    dashboard_link.click()

    page.get_by_role("heading", name="Card Cashback").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()  # Нажать на кнопку "копировать"
    page.wait_for_timeout(500)  # Подождать, пока скопируется
    copied_text = pyperclip.paste()
    print(f"Создана карта кешбек. UUID карты: {copied_text}")

    request.node.test_info = {
    "uuid": copied_text, "message": "Карта кешбек успешно создана!"
    }