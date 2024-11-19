import pytest

from methods.auth_methods import AuthMethods
from precondition.user_precondition import setup_data_user


@pytest.fixture
def create_user():
    auth = AuthMethods()
    user_credentials = setup_data_user()
    response = auth.register_user(user_credentials)
    yield user_credentials
    token = {"Authorization": response.json()["accessToken"]}
    auth.delete_user(token)


@pytest.fixture
def create_and_token_user():
    auth = AuthMethods()
    user_credentials = setup_data_user()
    response = auth.register_user(user_credentials)
    token = {"Authorization": response.json()["accessToken"]}
    yield token, user_credentials
    auth.delete_user(token)
