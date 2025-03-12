import allure


@allure.step("Проверка статус кода и ответа.")
def check_status_code(
        expected_status_code: int,
        actual_status_code: int,
):
    assert actual_status_code == expected_status_code
