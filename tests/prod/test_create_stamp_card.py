import re
import os
import random
import pyperclip
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

    page.get_by_role("link").filter(has_text=re.compile(r"^$")).nth(1).click()
    page.get_by_role("button", name="Icon Member").click()
    page.get_by_role("button", name="Icon Stamp", exact=True).click()
    page.get_by_role("textbox", name="Card Name").click()
    page.get_by_role("textbox", name="Card Name").fill("stamp")
    page.get_by_role("button", name="Recard Me").click()
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#9c8dd3")
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

    page.get_by_role("heading", name="Our Stamp Icons").click()
    page.get_by_role("button", name="Pizza").click()
    page.get_by_text("Waffles").click()
    page.locator("label").filter(has_text="Upload Custom Stamp Icon").locator(
        "div"
    ).first.click()
    page.locator("label").filter(has_text="Upload Custom Stamp Icon").locator(
        "input[type='file']"
    ).set_input_files(stamp_icon_path)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Continue").click()
""" 
    Уровни для штампов
    page.get_by_role("button", name="✏️").click()
    page.get_by_role("textbox", name="e.g. Bonus Stamp").click()
    page.get_by_role("textbox", name="e.g. Bonus Stamp").fill("1")
    page.locator('input[name="cardColor"]').first.click()
    page.locator('input[name="cardColor"]').first.fill("#a3cc0f")
    page.locator("label").filter(has_text="Text").click()
    page.get_by_role("textbox", name="% off coffee").click()
    page.get_by_role("textbox", name="% off coffee").fill("Pepsi cola")
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("")
    page.get_by_role("spinbutton").dblclick()
    page.get_by_role("spinbutton").fill("1")
    page.get_by_role("spinbutton").dblclick()
    page.get_by_role("spinbutton").dblclick()
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("button", name="➕ Add").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("button", name="×").click()
    page.get_by_role("button", name="Continue").click()
"""
    page.get_by_role("button", name="5", exact=True).click()
    page.get_by_role("button", name="6", exact=True).click()
    page.get_by_role("button", name="Continue").click()

    page.locator("div").filter(has_text=re.compile(r"^E-mail$")).first.click()
    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Enter name").click()
    page.get_by_role("textbox", name="Enter name").fill("favorite coffee")
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("latte")
    page.locator("div").filter(
        has_text=re.compile(r"^Field TypeCustomField nameChoice Options Required$")
    ).get_by_role("button").nth(1).click()
    page.get_by_role("textbox", name="Enter option name").click()
    page.get_by_role("textbox", name="Enter option name").fill("capuchino")
    page.locator("div").filter(
        has_text=re.compile(r"^Field TypeCustomField nameChoice Optionslatte Required$")
    ).get_by_role("button").nth(2).click()
    page.get_by_role("button", name="Add").nth(1).click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Full Name").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_text("Gift Stamps").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Stamps left").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("instagramm")
    page.locator("div").filter(has_text=re.compile(r"^common\.selectPlaceholder$")).nth(
        2
    ).click()
    page.get_by_text("Description", exact=True).click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").click()
    page.get_by_role("textbox", name="Mon-Sun: 10:00 - 20:").fill(
        "https://youtu.be/w2DZA3mfAUU?feature=shared"
    )
    page.get_by_role("textbox", name="Opening hours").click()
    page.get_by_role("textbox", name="Opening hours").fill("abc")
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="% discount").click()
    page.get_by_role("textbox", name="% discount").fill("55")
    page.get_by_role("textbox", name="Type an address or a place").click()
    page.get_by_role("textbox", name="% discount").click()
    page.get_by_role("textbox", name="% discount").fill("55 discount")
    page.get_by_role("textbox", name="Type an address or a place").click()
    page.get_by_role("textbox", name="Type an address or a place").fill("bishkek")
    page.get_by_text("Bishkek City Kyrgyzstan").click()
    page.locator("button").filter(has_text=re.compile(r"^Add$")).click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()

    page.get_by_role("link", name="Go to Dashboard").click()
    page.get_by_role("heading", name="Card stamp").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    page.get_by_role("button").filter(
        has_text=re.compile(r"^$")
    ).click()  # Нажать на кнопку "копировать"
    page.wait_for_timeout(500)  # Подождать, пока скопируется
    copied_text = pyperclip.paste()
    print(f"Создана карта штампы. UUID карты: {copied_text}")

    request.node.test_info = {"message": f"Создана карта штампы!\nUUID: {copied_text}"}
