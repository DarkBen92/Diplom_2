import requests
import allure

from data import BASE_URL, ORDERS_URL


class OrderMethods:
    @allure.step("Создание заказа")
    def create_order(self, headers, params):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", headers=headers, json=params)
        return response

    @allure.step("Получение заказов")
    def get_order(self, headers):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}", headers=headers)
        return response
