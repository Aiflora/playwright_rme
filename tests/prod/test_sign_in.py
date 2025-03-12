import pytest
import re
from playwright.sync_api import sync_playwright, expect

def test_sign_in():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

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

        # Проверка успешной авторизации
        expect(page.get_by_role("button", name="Мой аккаунт А")).to_be_visible()

        print(f"Существующий пользователь вошёл в свой аккаунт. Использованный email: aigerimkalil9@gmail.com")

        context.close()
        browser.close()

if __name__ == "__main__":
    pytest.main()

