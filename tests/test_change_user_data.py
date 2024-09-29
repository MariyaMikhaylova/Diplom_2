import allure

from burger_api import BurgerApi
from data import TestUserData
from helper import TestDataHelper


class TestChangeUserData:

    @allure.title('Проверка успешного изменения email')
    def test_successful_change_user_email(self, user_data, user_token):
        new_email = TestDataHelper.generate_email(3)
        request_body = TestDataHelper.create_change_user_data_body(new_email, user_data['password'], user_data['name'])
        data_change_response = BurgerApi.change_user_data(request_body, user_token)
        response_body = data_change_response.json()
        assert (data_change_response.status_code == 200
                and response_body['success']
                and response_body['user']['email'] == new_email
                and response_body['user']['name'] == user_data['name'])

    @allure.title('Проверка успешного изменения имени')
    def test_successful_change_user_name(self, user_data, user_token):
        new_name = TestDataHelper.generate_name(3)
        request_body = TestDataHelper.create_change_user_data_body(user_data['email'], user_data['password'], new_name)
        data_change_response = BurgerApi.change_user_data(request_body, user_token)
        response_body = data_change_response.json()
        assert (data_change_response.status_code == 200
                and response_body['success']
                and response_body['user']['email'] == user_data['email']
                and response_body['user']['name'] == new_name)

    @allure.title('Проверка успешного изменения пароля')
    def test_successful_change_user_password(self, user_data, user_token):
        new_password = TestDataHelper.generate_password(8)
        request_body = TestDataHelper.create_change_user_data_body(user_data['email'], new_password, user_data['name'])
        BurgerApi.change_user_data(request_body, user_token)
        login_body = TestUserData.LOGIN_USER_BODY.copy()
        login_body['email'] = user_data['email']
        login_body['password'] = new_password
        login_response = BurgerApi.login_user(login_body)
        response_body = login_response.json()
        assert (login_response.status_code == 200
                and response_body['success']
                and response_body['user']['email'] == user_data['email']
                and response_body['user']['name'] == user_data['name'])

    @allure.title('Проверка ошибки при изменении email, пароля или имени неавторизованным пользователем')
    def test_change_user_data_unauthorized_error(self):
        request_body = TestDataHelper.create_change_user_data_body(TestDataHelper.generate_email(3),
                                                                   TestDataHelper.generate_password(7),
                                                                   TestDataHelper.generate_name(3))
        error_data_change_response = BurgerApi.change_user_data(request_body, '')
        response_body = error_data_change_response.json()
        assert (error_data_change_response.status_code == 401
                and not response_body['success']
                and response_body['message'] == 'You should be authorised')
