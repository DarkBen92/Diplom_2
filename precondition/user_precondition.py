import allure

from data import generate_random_string


@allure.step("Подготовка данных для пользователя")
def setup_data_user():
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": f"{email}@yandex.ru",
        "password": f"{password}",
        "name": f"{name}"
    }
    return payload


@allure.step("Подготовка данных для авторизации")
def setup_authorization_user(data_user):
    payload = {
        "email": data_user["email"],
        "password": data_user["password"],
    }
    return payload
