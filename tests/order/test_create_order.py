import allure
import pytest

from methods.order_methods import OrderMethods
from precondition.order_precondition import setup_ingredients, setup_random_hash_ingredient
from conftest import create_and_token_user
from data import EMPTY_TOKEN


class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем.")
    def test_create_order_authorized_user(self, create_and_token_user):
        order = OrderMethods()
        response = order.create_order(
            headers=create_and_token_user[0],
            params=setup_ingredients()
        )
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа неавторизованным пользователем.")
    def test_create_order_unauthorized_user(self):
        order = OrderMethods()
        response = order.create_order(
            headers=EMPTY_TOKEN,
            params=setup_ingredients()
        )
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа с неверной передачей ингредиентов.")
    @pytest.mark.parametrize(
        "ingredients", [
            {"ingredients": []},
            setup_random_hash_ingredient()
        ]
    )
    def test_create_order_failed_ingredients(self, create_and_token_user, ingredients):
        order = OrderMethods()
        response = order.create_order(
            headers=create_and_token_user[0],
            params=ingredients
        )
        assert response.status_code == 400 and response.json()["success"] is False
