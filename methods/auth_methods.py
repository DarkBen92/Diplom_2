import requests
import allure

from data import BASE_URL, AUTH_URL


class AuthMethods:
    @allure.step("Регистрация пользователя")
    def register_user(self, params):
        response = requests.post(f"{BASE_URL}{AUTH_URL}register", json=params)
        return response

    @allure.step("Авторизация пользователя")
    def authorization_user(self, params):
        response = requests.post(f"{BASE_URL}{AUTH_URL}login", json=params)
        return response

    @allure.step("Обновления данных о пользователе")
    def update_user(self, headers, params):
        response = requests.patch(f"{BASE_URL}{AUTH_URL}user", headers=headers, json=params)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, headers):
        response = requests.delete(f"{BASE_URL}{AUTH_URL}user", headers=headers)
        return response
