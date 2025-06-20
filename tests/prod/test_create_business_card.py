import re
import os
import random
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


def test_create_business(page_with_video, request) -> None:
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
    page.get_by_role("button", name="Icon Business").click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("Business")
    page.get_by_role("button", name="Recard Me").click()

    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#000000")
    page.locator('[id="__next"] div').filter(
        has_text="Choose your card colors.Pick"
    ).nth(2).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_text("Upload Logo").click()
    page.get_by_text("Upload Banner").click()
    page.get_by_text("Logo for Notifications").click()
    page.get_by_role("button", name="Continue").click()

    page.locator("label > .absolute").first.click()
    page.locator(".flex > .grid").first.click()
    page.get_by_role("button", name="Delete Icon").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Empty").first.click()
    page.locator("div").filter(has_text=re.compile(r"^EmptyEmptyCustom$")).get_by_role(
        "button"
    ).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_text("Upload Logo").click()
    page.locator("label div").first.click()
    # Находим input внутри нужного блока Upload Logo
    upload_logo_input = page.locator(
        "div", has_text=re.compile(r"^Upload Logo")
    ).locator("input[type='file']")
    upload_logo_input.set_input_files(logo_path)

    page.wait_for_timeout(1000)

    page.get_by_role("textbox", name="Full name").click()
    page.get_by_role("textbox", name="Full name").fill("Test")
    page.locator(".ql-editor").first.click()
    page.locator(".ql-editor").first.fill("Recardme auto test")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("test")
    page.get_by_text("common.selectPlaceholder").click()
    page.get_by_text("Description", exact=True).click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill("testing")
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()

    page.get_by_role("link", name="Go to Dashboard").click()

    page.get_by_role("heading", name="Card Business").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    page.get_by_role("button").filter(
        has_text=re.compile(r"^$")
    ).click()  # Нажать на кнопку "копировать"
    page.wait_for_timeout(500)  # Подождать, пока скопируется
    copied_text = pyperclip.paste()
    print(f"Создана бизнес карта. UUID карты: {copied_text}")

    request.node.test_info = {"message": f"Создана бизнес карта!\nUUID: {copied_text}"}
