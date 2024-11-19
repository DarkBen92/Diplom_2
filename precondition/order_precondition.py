import allure


@allure.step("Подготовка ингредиентов")
def setup_ingredients():
    payload = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa71",
            "61c0c5a71d1f82001bdaaa78"
        ]
    }
    return payload


@allure.step("Подготовка несуществующего ингредиента")
def setup_random_hash_ingredient():
    payload = {
        "ingredients": [
            "71c0c5a71d1f82001bdaaa67"
        ]
    }
    return payload
