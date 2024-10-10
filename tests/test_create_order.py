import allure

from burger_api import BurgerApi
from helper import TestDataHelper


class TestCreateOrder:

    @allure.title('Проверка ошибки при создании заказа без ингредиентов')
    def test_create_order_empty_ingredient_list(self):
        request_body = TestDataHelper.create_empty_order_body()
        create_order_response = BurgerApi.create_order(request_body)
        response_body = create_order_response.json()
        assert (create_order_response.status_code == 400
                and not response_body["success"]
                and response_body["message"] == "Ingredient ids must be provided")

    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_create_order_authorized(self, user_data, user_login):
        request_body = TestDataHelper.create_order_body()
        create_order_response = BurgerApi.create_order(request_body)
        response_body = create_order_response.json()
        assert (create_order_response.status_code == 200
                and response_body["success"]
                and response_body["name"] is not None
                and response_body["order"]["number"] > 0)

    @allure.title('Проверка успешного создания заказа неавторизованным пользователем')
    def test_create_order_unauthorized(self):
        request_body = TestDataHelper.create_order_body()
        create_order_response = BurgerApi.create_order(request_body)
        response_body = create_order_response.json()
        assert (create_order_response.status_code == 200
                and response_body["success"]
                and response_body["name"] is not None
                and response_body["order"]["number"] > 0)

    @allure.title('Проверка успешного создания заказа с несколькими ингредиентами')
    def test_create_order_with_ingredients(self):
        request_body = TestDataHelper.create_order_body()
        request_body["ingredients"].append("61c0c5a71d1f82001bdaaa6f")
        request_body["ingredients"].append("61c0c5a71d1f82001bdaaa6e")
        request_body["ingredients"].append("61c0c5a71d1f82001bdaaa7a")
        create_order_response = BurgerApi.create_order(request_body)
        response_body = create_order_response.json()
        assert (create_order_response.status_code == 200
                and response_body["success"]
                and response_body["name"] is not None
                and response_body["order"]["number"] > 0)

    @allure.title('Проверка ошибки при создании заказа с несколькими ингредиентами')
    def test_create_order_wrong_ingredient_id(self):
        request_body = TestDataHelper.create_empty_order_body()
        request_body["ingredients"].append("test123test")
        create_order_response = BurgerApi.create_order(request_body)
        assert create_order_response.status_code == 500
