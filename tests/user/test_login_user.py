import allure
from methods.auth_methods import AuthMethods
from precondition.user_precondition import setup_authorization_user
from conftest import create_user


class TestLoginUser:

    @allure.title("Успешная авторизация пользователя.")
    def test_login_user_success(self, create_user):
        auth = AuthMethods()
        response = auth.authorization_user(setup_authorization_user(create_user))
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Попытка авторизации пользователя с неверным логином и паролем.")
    def test_login_user_invalid_login_and_password(self, create_user):
        auth = AuthMethods()
        create_user["email"] = "not_email@yandex.ru"
        create_user["password"] = "111"
        response = auth.authorization_user(setup_authorization_user(create_user))
        assert response.status_code == 401 and response.json()["success"] is False
