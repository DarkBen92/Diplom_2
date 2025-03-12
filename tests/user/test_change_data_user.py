import allure

from methods.auth_methods import AuthMethods
from precondition.user_precondition import setup_authorization_user, setup_data_user
from conftest import create_and_token_user
from steps import user_steps


class TestChangeDataUser:
    @allure.title("Успешная изменение данных пользователя.")
    def test_change_data_user(self, create_and_token_user):
        auth = AuthMethods()
        new_data = setup_data_user()
        response = auth.update_user(
            headers=create_and_token_user[0],
            params=setup_authorization_user(new_data)
        )
        user_steps.check_status_code(
            expected_status_code=200,
            actual_status_code=response.status_code
        )
        # assert response.json()["success"] is True

    @allure.title("Попытка изменение данных неавторизованного пользователя.")
    def test_change_data_user_not_authorization(self):
        auth = AuthMethods()
        new_data = setup_data_user()
        response = auth.update_user(
            headers={"test": "test"},
            params=setup_authorization_user(new_data)
        )
        assert response.status_code == 401 and response.json()["success"] is False
