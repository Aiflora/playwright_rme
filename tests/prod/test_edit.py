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
 
def test_(page: Page) -> None:
    # Генерация случайных изображений перед 0
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

    page.locator("div:nth-child(12) > .py-2 > .absolute > .px-3").first.click()
    page.get_by_role("link", name="Edit card").click()

    page.get_by_role("textbox", name="Recardme").click()
    page.get_by_role("textbox", name="Recardme").fill("Кешбек кешбек")
    page.get_by_role("textbox", name="Recardme").click()
    page.get_by_label("", exact=True).first.click()
    page.get_by_label("", exact=True).first.fill("#ff80f4")
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#118357")
    page.get_by_text("Name of the CardCard").click()
    page.get_by_text("Upload Logo").click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("div").first.click()
    page.locator("label").filter(has_text="Recommended dimensions:Rectangular: 480 x 150 pixelsSquare: 150 x 150 pixels").locator("input[type='file']").set_input_files(logo_path)
    page.get_by_text("Upload Banner").click()
    page.get_by_text("Logo for Notifications").click()
    page.get_by_role("button", name="Full Name").click()
    page.get_by_role("button", name="Full Name").click()
    page.get_by_role("button", name="Tier").click()
    page.get_by_role("button", name="Tier").click()
  # page.get_by_role("button", name="Balance").wait_for(state="visible", timeout=30000).click()
    page.get_by_text("Total Spent").click()
    page.get_by_text("Total Spent").click()
    page.get_by_role("spinbutton").first.click()
    page.get_by_role("spinbutton").first.fill("10")
    page.get_by_role("spinbutton", name="Days Until Expiration").click()
    page.get_by_role("spinbutton", name="Days Until Expiration").fill("5")
    page.get_by_role("spinbutton", name="Days Before Expiration to").click()
    page.get_by_role("spinbutton", name="Days Before Expiration to").fill("0")
    page.get_by_role("textbox", name="Notification Message").click()
    page.locator("div").filter(has_text=re.compile(r"^Bonus expiry settings$")).click()
    page.get_by_role("textbox", name="Notification Message").click()
    page.get_by_role("textbox", name="Notification Message").fill("bonus will delete")
    page.get_by_role("heading", name="Change the discount levels").click()
    page.get_by_role("button", name="Add").first.click()
    page.get_by_role("textbox", name="Gold").click()
    page.get_by_role("textbox", name="Gold").fill("edit test")
    page.get_by_placeholder("100").click()
    page.get_by_placeholder("100").fill("100000")
    page.get_by_placeholder("5").click()
    page.get_by_placeholder("5").fill("99")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("textbox", name="USD").fill("USD")
    page.get_by_role("textbox", name="USD").click()
    page.get_by_role("button", name="add dynamic cashback").click()
    page.locator("div").filter(has_text=re.compile(r"^Percentage %start timeend timeupdate dynamic cashback$")).get_by_placeholder("5").click()
    page.locator("div").filter(has_text=re.compile(r"^Percentage %start timeend timeupdate dynamic cashback$")).get_by_placeholder("5").fill("65")
    page.get_by_role("heading", name="start time").click()
    page.locator("input[name=\"start_time\"]").click()
    page.locator("input[name=\"start_time\"]").fill("07:07")
    page.locator("input[name=\"end_time\"]").click()
    page.get_by_role("heading", name="end time").click()
    page.locator("input[name=\"end_time\"]").click()
    page.locator("input[name=\"end_time\"]").fill("22:22")
    page.locator("form").get_by_role("button", name="Add", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Customize the percentage of points deducted%Add$")).get_by_role("spinbutton").click()
    page.locator("div").filter(has_text=re.compile(r"^Customize the percentage of points deducted%Add$")).get_by_role("spinbutton").fill("100")
    page.get_by_text("%Add").click()
    page.locator(".mb-5 > div > div:nth-child(2) > button:nth-child(2)").first.click()
    page.locator("body").press("F6")
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Success!").click()
