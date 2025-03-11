from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def test_recardme_flow(page):
    page.goto("https://www.recardme.com/")
    page.locator("label").filter(has_text="Русский").locator("span").nth(1).click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("link", name="Вход").click()
    page.locator("#email").click()
    page.locator("#email").fill("aigerimkalil9@gmail.com")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("A200200052!")
    page.get_by_role("button", name="Вход").click()
    page.locator(".p-5 > div > a").click()
    page.get_by_role("button", name="Icon Кешбек карта").click()
    page.get_by_role("textbox", name="Название карты").click()
    page.get_by_role("textbox", name="Название карты").click()
    page.get_by_role("textbox", name="Название карты").fill("кешбек карта")
    page.get_by_role("button", name="Recard Me").click()
    page.get_by_label("", exact=True).nth(2).click()
    page.get_by_label("", exact=True).nth(2).fill("#20ac64")
    page.locator("[id=\"__next\"] div").filter(has_text="Выберите цвета вашей карты.Выберите цвет вашей открытки и текста. После того, ка").nth(2).click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Продолжить").click()
    page.locator("label > .absolute").first.click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Имя Фамилия").click()
    page.get_by_role("button", name="Empty").first.click()
    page.get_by_role("listitem").filter(has_text="Телефон").click()
    page.get_by_role("button", name="Empty").click()
    page.get_by_text("Уровень").click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Продолжить").click()
    page.get_by_role("button", name="Завершить").click()
    page.get_by_role("link", name="Перейти к панели управления").click()