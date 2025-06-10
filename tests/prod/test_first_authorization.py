import pytest
import re
import secrets
import string
from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

def generate_random_password(length=10):
    """Генерирует случайный пароль с буквами, цифрами и спецсимволами."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

def test_first_authorization(page: Page) -> None:
    email = fake.email()
    password = generate_random_password()

def test_first_authorization(page_with_video, request) -> None:
    page = page_with_video
    email = fake.email()
    password = generate_random_password()
    
    page.goto("https://www.recardme.com/")

    page.locator("label").filter(has_text="English").click()
    page.get_by_role("button", name="Confirm").click()
    page.locator(".w-full > .flex > .btn").click()
    page.locator("input[name=\"companyName\"]").click()
    page.locator("input[name=\"companyName\"]").fill("Test")
    page.get_by_placeholder("First name").click()
    page.get_by_placeholder("First name").fill("Test")
    page.get_by_placeholder("Last name").click()
    page.get_by_placeholder("Last name").fill("Test")
    page.locator("#email").click()
    page.locator("#email").fill(email)
    page.locator("label").filter(has_text="InternationalAfghanistanÅland").get_by_role("textbox").click()
    page.locator("label").filter(has_text="InternationalAfghanistanÅland").get_by_role("textbox").fill("+996 500 197 347")
    page.get_by_placeholder("Password", exact=True).click()
    page.get_by_placeholder("Password", exact=True).fill(password)
    page.get_by_placeholder("Repeat password").click()
    page.get_by_placeholder("Repeat password").fill(password)
    page.get_by_role("button", name="Sign up").click()
    page.get_by_role("link", name="To home").click()
    page.locator(".w-full > .flex > .btn").click()
    page.get_by_role("button", name="My account T").click()
    page.get_by_role("link", name="Account Details").click()
    page.wait_for_timeout(500)
    

    request.node.test_info = {
        "message": f"Авторизован новый пользователь\nИспользованный email: {email}\nПароль: {password}"
    }
