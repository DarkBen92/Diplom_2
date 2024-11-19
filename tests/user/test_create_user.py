import allure

from methods.auth_methods import AuthMethods
from precondition.user_precondition import setup_data_user
from data import delete_field


class TestCreateUser:

    @allure.title("Успешное создание пользователя.")
    def test_create_user_success(self):
        auth = AuthMethods()
        response = auth.register_user(setup_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Повторное создание пользователя.")
    def test_create_double_user(self):
        auth = AuthMethods()
        first_user = setup_data_user()
        auth.register_user(first_user)
        response = auth.register_user(first_user)
        assert response.status_code == 403 and response.json()["success"] is False

    @allure.title("Попытка создать пользователя не имея почты.")
    def test_create_no_login_user(self):
        auth = AuthMethods()
        request_without_email = delete_field(setup_data_user(), "email")
        response = auth.register_user(request_without_email)
        assert response.status_code == 403 and response.json()["success"] is False
