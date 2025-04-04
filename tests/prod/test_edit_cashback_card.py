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

    page.get_by_role("link", name="Open Кешбек кешбек а |").click()
    page.get_by_role("link", name="Edit card").click()
    page.get_by_role("heading", name="Name of the Card").click()
    page.get_by_role("textbox", name="Recardme").click()
    page.get_by_role("heading", name="Card colors").click()
    page.get_by_label("", exact=True).first.click()
    page.get_by_label("", exact=True).first.fill("#f2abeb")
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#1f372e")
    page.get_by_text("Image uploadUpload").click()
    page.get_by_role("heading", name="Image upload").click()
    page.get_by_role("heading", name="Image upload").click()
    page.get_by_text("Upload Logo").click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("input[type='file']").set_input_files(logo_path)
    page.get_by_text("Upload Banner").click()
    page.get_by_text("Logo for Notifications").click()
    page.get_by_role("heading", name="Card fields").click()
    page.get_by_role("heading", name="Top Right").click()
    page.get_by_role("heading", name="Bottom Left").click()
    page.get_by_role("heading", name="Bottom Right").click()
    page.get_by_role("button", name="Phone").click()
    page.get_by_role("listitem").filter(has_text="Full Name").click()
    page.get_by_role("heading", name="Initial Balance").click()
    page.get_by_role("heading", name="Bonus expiry settings").click()
    page.get_by_text("Days Until Expiration").click()
    page.get_by_text("Days Before Expiration to").click()
    page.get_by_text("Notification Message").click()
    page.get_by_role("heading", name="Change the discount levels").click()
    page.get_by_role("heading", name="Tier").click()
    page.get_by_role("heading", name="Money Amount").click()
    page.get_by_role("heading", name="Percentage", exact=True).click()
    page.get_by_role("heading", name="Currency").click()
    page.get_by_role("heading", name="Customize the percentage of").click()
    page.locator("div").filter(has_text=re.compile(r"^Customize the percentage of points deducted%Add$")).get_by_role("spinbutton").click()
    page.get_by_role("heading", name="Back Side Info").click()
    page.get_by_role("heading", name="Delete", exact=True).click()
    page.get_by_role("link", name="Enrollment").click()
    page.get_by_role("heading", name="Edit Card Text").click()
    page.get_by_role("heading", name="Form Title").click()
    page.get_by_role("heading", name="Form Description").click()
    page.get_by_role("heading", name="Card color").click()
    page.get_by_text("Text", exact=True).click()
    page.locator("input[name=\"color\"]").first.click()
    page.locator("input[name=\"color\"]").first.fill("#973030")
    page.get_by_text("Background").click()
    page.locator("input[name=\"background\"]").first.click()
    page.locator("input[name=\"background\"]").first.fill("#7c5054")
    page.get_by_role("heading", name="Image upload").click()
    page.get_by_role("heading", name="Terms Of Conditions").click()
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").fill("Сохранение и обработка данныхdfgdgdgdgd.")
    # page.locator("label").filter(has_text="Upload LogoRecommended").locator("path").click()
    page.get_by_role("main").first.click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Success!").click()
    #page.get_by_role("link", name="cards Card").click()

    print(f"Изменения в кешбэк карте лого поменяли.")
