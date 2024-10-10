import allure
import pytest

from burger_api import BurgerApi
from helper import TestDataHelper


class TestCreateUser:

    @allure.title('Проверка успешной регистрации пользователя')
    def test_successful_registration_user(self):
        registration_body = TestDataHelper.create_registration_body()
        registration_response = BurgerApi.create_user(registration_body)
        response_body = registration_response.json()
        assert (registration_response.status_code == 200
                and response_body['success']
                and response_body['user']['email'] == registration_body['email']
                and response_body['user']['name'] == registration_body['name']
                and response_body['accessToken'] is not None
                and response_body['refreshToken'] is not None)

    @allure.title('Проверка ошибки при повторной регистрации пользователя')
    def test_registration_user_twice(self):
        registration_body = TestDataHelper.create_registration_body()
        BurgerApi.create_user(registration_body)
        registration_error_response = BurgerApi.create_user(registration_body)
        response_body = registration_error_response.json()
        assert (registration_error_response.status_code == 403
                and not response_body['success']
                and response_body['message'] == 'User already exists')

    @allure.title('Проверка ошибки при попытке регистрации пользователя без email, пароля или имени')
    @pytest.mark.parametrize('invalid_body', [TestDataHelper.create_registration_body_without_email(),
                                              TestDataHelper.create_registration_body_without_password(),
                                              TestDataHelper.create_registration_body_without_name()])
    def test_registration_user_without_data(self, invalid_body):
        registration_body = invalid_body
        registration_response = BurgerApi.create_user(registration_body)
        response_body = registration_response.json()
        assert (registration_response.status_code == 403
                and not response_body['success']
                and response_body['message'] == 'Email, password and name are required fields')
