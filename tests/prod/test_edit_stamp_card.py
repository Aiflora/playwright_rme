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

    page.locator("div:nth-child(4) > .py-2 > .absolute > .px-3").first.click()
    page.get_by_role("link", name="Edit card").click()
    page.get_by_role("heading", name="Name of the Card").click()
    page.get_by_role("textbox", name="Recardme").click()
    page.get_by_role("heading", name="Card colors").click()
    page.get_by_role("textbox", name="Recardme").click()
    page.get_by_role("textbox", name="Recardme").fill("stamp 1")
    page.get_by_role("heading", name="Card colors").click()
    page.get_by_label("", exact=True).first.click()
    page.get_by_label("", exact=True).first.fill("#1f2cdb")
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#b0a5d9")
    page.get_by_text("Background").click()
    page.get_by_role("heading", name="Image upload").click()
    page.get_by_text("Upload Logo").click()
    page.get_by_text("Upload Banner").click()
    page.get_by_text("Logo for Notifications").click()
    page.get_by_role("heading", name="Card fields").click()
    page.get_by_role("heading", name="Card fields").click()
    page.get_by_role("heading", name="Bottom Left").click()
    page.get_by_role("heading", name="Bottom Right").click()
    # page.get_by_role("button", name="Full Name").click()
    # page.get_by_text("Phone").click()
    # page.get_by_role("heading", name="Stamp Icon", exact=True).click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Waffles").click()
    page.get_by_text("Upload Custom Stamp Icon").click()
    page.get_by_role("heading", name="Stamps Count").click()
    page.get_by_role("button", name="10").click()
    page.get_by_role("heading", name="Delete", exact=True).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Success!").click()
    page.get_by_role("link", name="Enrollment").click()
    page.get_by_role("heading", name="Edit Card Text").click()
    page.get_by_role("heading", name="Form Title").click()
    page.get_by_role("heading", name="Form Description").click()
    page.get_by_role("heading", name="Card color").click()
    page.get_by_text("Background").click()
    page.get_by_text("Text", exact=True).click()
    page.locator("input[name=\"color\"]").first.click()
    page.locator("input[name=\"color\"]").first.fill("#15c6a3")
    page.get_by_text("Background").click()
    page.locator("input[name=\"background\"]").first.click()
    page.locator("input[name=\"background\"]").first.fill("#8dd3b8")
    page.get_by_role("heading", name="Image upload").click()
    page.get_by_role("heading", name="Edit Card Fields").click()
    page.locator(".relative > .absolute").first.click()
    page.get_by_role("heading", name="Terms Of Conditions").click()
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").press("ArrowRight")
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").press("ArrowRight")
    page.get_by_text("Сохранение и обработка данных").fill("Сохранение и обработка данных. ")
    page.get_by_text("Сохранение и обработка данных").click()
    page.get_by_text("Сохранение и обработка данных").fill("Сохранение и обработка данных. 1")
    page.get_by_text("Сохранение и обработка данных").press("ArrowRight")
    page.get_by_text("Сохранение и обработка данных.").press("ArrowRight")
    page.get_by_text("Сохранение и обработка данных.").press("ArrowRight")
    page.get_by_text("Сохранение и обработка данных.").fill("Сохранение и обработка данных. 123")
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Success!").click()
    # page.get_by_role("link", name="cards Card").click()