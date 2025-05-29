import re
import requests
import os
import pyperclip
from playwright.sync_api import Page, expect


def test_sign_in(page_with_video, request) -> None:
    page = page_with_video
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="English").locator("span").nth(1).click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("link", name="Sign in").click()
    page.locator("#email").click()
    page.locator("#email").fill("test_prod@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("A200200052!")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="My account t").click()
    page.get_by_role("link", name="Account Details").click()
    page.get_by_role("heading", name="test").click()
    page.wait_for_timeout(400)

    request.node.test_info = {
        "message": "Существующий пользователь зашёл на свой аккаунт Использованный email: test_prod@gmail.com"
    }