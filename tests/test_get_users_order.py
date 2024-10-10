import allure

from burger_api import BurgerApi


class TestGetUsersOrder:

    @allure.title('Проверка успешного получения скиска заказов зарегистрированного пользователя')
    def test_get_order_list_authorized(self, user_token, create_order_authorized):
        get_order_list = BurgerApi.get_users_order(user_token)
        response_body = get_order_list.json()
        assert (get_order_list.status_code == 200
                and response_body["success"]
                and response_body["orders"][0]["_id"] == create_order_authorized["order"]["_id"]
                and response_body["total"] > 0
                and response_body["totalToday"] > 0)

    @allure.title('Проверка ошибки при попытке получения скиска заказов незарегистрированным пользователем')
    def test_get_order_list_unauthorized(self):
        get_order_list = BurgerApi.get_users_order('')
        response_body = get_order_list.json()
        assert (get_order_list.status_code == 401
                and not response_body["success"]
                and response_body["message"] == "You should be authorised")
