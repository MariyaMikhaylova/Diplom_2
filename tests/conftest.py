import pytest

from burger_api import BurgerApi
from data import TestUserData
from helper import TestDataHelper


@pytest.fixture(scope='function')
def user_registration(user_data):
    registration_body = TestUserData.REGISTRATION_USER_BODY.copy()
    registration_body['email'] = user_data['email']
    registration_body['name'] = user_data['name']
    registration_body['password'] = user_data['password']
    registration_response = BurgerApi.create_user(registration_body)
    yield registration_response
    BurgerApi.delete_user(registration_response.json()['accessToken'])


@pytest.fixture(scope='function')
def user_login(user_data, user_registration):
    login_body = TestUserData.LOGIN_USER_BODY.copy()
    login_body['email'] = user_data['email']
    login_body['password'] = user_data['password']
    login_response = BurgerApi.login_user(login_body)
    return login_response


@pytest.fixture(scope='function')
def user_data():
    data = TestUserData.USER_DATA.copy()
    data['email'] = TestDataHelper.generate_email(7)
    data['password'] = TestDataHelper.generate_password(7)
    data['name'] = TestDataHelper.generate_name(7)
    return data


@pytest.fixture(scope='function')
def user_token(user_login):
    return user_login.json()['accessToken']


@pytest.fixture(scope='function')
def create_order_authorized(user_data, user_token):
    request_body = TestDataHelper.create_order_body()
    create_order_response = BurgerApi.create_order_authorized(request_body, user_token)
    response_body = create_order_response.json()
    return response_body
