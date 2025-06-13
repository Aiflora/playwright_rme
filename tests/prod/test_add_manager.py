"""
import re
import os
import pytest
import random
import pyperclip
import time
from playwright.sync_api import Page, expect
from PIL import Image, ImageDraw


def test_example(page: Page) -> None:
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="English").locator("span").nth(2).click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("link", name="Sign in").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("A200200052!")
    page.get_by_role("button", name="Sign in").click()


    nav = page.locator('nav.flex.flex-col')
    nav.hover()

    link = page.locator('a[href="/ru/dashboard/managers"]')
    link.wait_for(state="visible", timeout=5000)
    link.click()

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("textbox", name="example@gmail.com").click()
    page.get_by_role("textbox", name="example@gmail.com").fill("testings@")
    page.get_by_role("textbox", name="example@gmail.com").click()
    page.get_by_role("textbox", name="example@gmail.com").fill("testings@gmail.com")
    page.get_by_role("textbox", name="example@gmail.com").click()
    page.get_by_role("textbox", name="example@gmail.com").press("ArrowLeft")
    page.get_by_role("textbox", name="example@gmail.com").press("ArrowLeft")
    page.get_by_role("textbox", name="example@gmail.com").press("ArrowLeft")
    page.get_by_role("textbox", name="example@gmail.com").press("ArrowLeft")
    page.get_by_role("textbox", name="example@gmail.com").fill("testings123@gmail.com")
    page.get_by_role("textbox", name="example@gmail.com").click()
    page.get_by_role("button", name="Undo").click()
    page.get_by_role("button", name="SelectAll").click()
    page.get_by_role("button", name="Undo").click()
    page.get_by_role("button", name="SelectAll").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_text("Manager added successfully!").click()
    page.get_by_role("button", name="Edit").click()
    page.locator("div").filter(has_text=re.compile(r"^Edit$")).get_by_role("button").click()
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Updated user!").click()
"""

import re
import os
import random
import pyperclip
from playwright.sync_api import Page, expect
from PIL import Image, ImageDraw


def test_create_manager(page_with_video, request) -> None:
    page = page_with_video
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="English").locator("span").nth(2).click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("link", name="Sign in").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("A200200052!")
    page.get_by_role("button", name="Sign in").click()

    # Ждём навбар (родительский блок с классом nav.flex)
    navbar = page.locator("nav.flex")

    # Навести мышку на весь nav
    navbar.hover()

    # Находим все элементы с классом "navbar-item"
    navbar_items = page.locator("a.navbar-item")

    # Убедимся, что найдено как минимум 2 элемента
    expect(navbar_items).to_have_count(5)

    # Навести мышку на второй элемент (индексация с 0)
    navbar_items.nth(1).hover()

    # Клик по второму элементу
    navbar_items.nth(1).click()

    # Проверить переход по URL (по желанию) expect(page).to_have_url("/dashboard/managers")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("textbox", name="example@gmail.com").click()
    page.get_by_role("textbox", name="example@gmail.com").fill("ttteeesssttt@gmail.com")
    page.get_by_role("button", name="Undo").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="SelectAll").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Add").click()
    page.wait_for_timeout(3000)

    page.get_by_role("button", name="Edit").first.click()
    page.get_by_role("heading", name="Select Role").click()
    page.locator("div").filter(
        has_text=re.compile(r"^Select Roleselect\.\.\.$")
    ).locator("div").nth(3).click()
    page.get_by_text("all permissions").click()
    page.locator("div").filter(has_text=re.compile(r"^all permissions$")).nth(2).click()
    page.get_by_text("all permissions").nth(1).click()
    page.get_by_role("button", name="Save").click()

    page.get_by_role("alert").filter(has_text="Role assigned successfully!").click()
    page.wait_for_timeout(1000)
    page.get_by_text("Role assigned successfully!").click()
    page.wait_for_timeout(1000)
    page.get_by_text("Updated user!").click()

    page.get_by_role("button", name="Delete").click()
    page.wait_for_timeout(1000)
    page.get_by_text("Employee successfully deleted").click()
    page.wait_for_timeout(3000)

    print("Менеджер добавлен и удален успешно.")

    request.node.test_info = {"message": "Менеджер добавлен и удален успешно!"}
