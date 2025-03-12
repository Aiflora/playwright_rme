import pytest
import re
import secrets
import string
from faker import Faker
from playwright.sync_api import Page, expect

# Инициализация Faker для генерации случайных данных
fake = Faker()

def generate_random_password(length=10):
    """Генерирует случайный пароль с буквами, цифрами и спецсимволами."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

def test_registration(page: Page) -> None:
    # Генерация случайных данных
    email = fake.email()
    password = generate_random_password()

    # Открываем сайт
    page.goto("https://www.recardme.com/")

    # Выбор языка Русский и подтверждение
    page.locator("label").filter(has_text="Русский").locator("span").nth(1).click()
    page.get_by_role("button", name="Подтвердить").click()

    # Переход к регистрации
    page.locator(".w-full > .flex > .btn").click()

    # Заполнение формы регистрации
    page.locator("input[name=\"companyName\"]").fill(fake.company())
    page.get_by_placeholder("Имя").fill(fake.first_name())
    page.get_by_placeholder("Фамилия").fill(fake.last_name())
    page.locator("#email").fill(email)
    page.get_by_placeholder("Пароль", exact=True).fill(password)
    page.get_by_placeholder("Повторите пароль").fill(password)

    # Нажатие кнопки "Создать аккаунт"
    page.get_by_role("button", name="Создать аккаунт").click()

    # Проверяем, что мы перешли на главную страницу
    page.get_by_role("link", name="На главную").click()

    # Повторный вход на страницу регистрации
    page.locator(".w-full > .flex > .btn").click()

    print(f"Авторизован новый пользователь. Использованный email: {email} | Пароль: {password}")
