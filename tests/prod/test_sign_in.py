import re
import pytest
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="Русский").click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("link", name="Вход").click()
    page.locator("#email").click()
    page.locator("#email").fill("aigerimkalil9@gmail.com")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("A200200052!")
    page.get_by_role("button", name="Вход").click()
    page.get_by_role("button", name="Мой аккаунт А").click()
    page.get_by_role("link", name="Детали учетной записи").click()

    print(f"Существующий пользователь зашёл на свой аккаунт. Использованный email: aigerimkalil9@gmail.com | Пароль: A200200052!")