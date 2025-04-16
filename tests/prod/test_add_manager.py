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
    # page.get_by_role("link", name="cards Managers").click() 
    # page.pause()

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
