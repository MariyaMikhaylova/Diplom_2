import allure

from burger_api import BurgerApi
from data import TestUserData


class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_successful_login(self, user_data, user_login):
        user_login_response = user_login.json()
        assert (user_login.status_code == 200
                and user_login_response['success']
                and user_login_response['accessToken'] is not None
                and user_login_response['refreshToken'] is not None
                and user_login_response['user']['email'] == user_data['email']
                and user_login_response['user']['name'] == user_data['name'])

    @allure.title('Проверка ошибки при попытке авторизации с некорректным email')
    def test_invalid_email_login(self, user_data, user_registration):
        login_body = TestUserData.LOGIN_USER_BODY.copy()
        login_body['email'] = 'email@test.br'
        login_body['password'] = user_data['password']
        login_error_response = BurgerApi.login_user(login_body)
        response_body = login_error_response.json()
        assert (login_error_response.status_code == 401
                and not response_body['success']
                and response_body['message'] == 'email or password are incorrect')

    @allure.title('Проверка ошибки при попытке авторизации с некорректным паролем')
    def test_invalid_password_login(self, user_data, user_registration):
        login_body = TestUserData.LOGIN_USER_BODY.copy()
        login_body['email'] = user_data['email']
        login_body['password'] = 'password'
        login_error_response = BurgerApi.login_user(login_body)
        response_body = login_error_response.json()
        assert (login_error_response.status_code == 401
                and not response_body['success']
                and response_body['message'] == 'email or password are incorrect')
