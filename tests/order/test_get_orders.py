import allure

from methods.order_methods import OrderMethods
from conftest import create_and_token_user
from data import EMPTY_TOKEN


class TestGetOrders:
    @allure.title("Получение заказов авторизованным пользователем.")
    def test_get_orders_authorized_user(self, create_and_token_user):
        order = OrderMethods()
        response = order.get_order(headers=create_and_token_user[0])
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Попытка получения заказов неавторизованным пользователем.")
    def test_get_orders_unauthorized_user(self):
        order = OrderMethods()
        response = order.get_order(headers=EMPTY_TOKEN)
        assert response.status_code == 401 and response.json()["success"] is False
