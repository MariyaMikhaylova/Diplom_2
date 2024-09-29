import random
from data import TestUserData


class TestDataHelper:

    def generate_email(length):
        email = ""
        for i in range(length):
            email = email + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwz'))
        return f'{email}@test.br'

    def generate_password(length):
        password = ""
        for i in range(length):
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        return password

    def generate_name(length):
        name = ""
        for i in range(length):
            name = name + random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        return name

    @classmethod
    def create_registration_body(cls):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body['email'] = TestDataHelper.generate_email(7)
        body['password'] = TestDataHelper.generate_password(7)
        body['name'] = TestDataHelper.generate_name(7)
        return body

    @classmethod
    def create_registration_body_without_email(cls):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body['email'] = ''
        body['password'] = TestDataHelper.generate_password(7)
        body['name'] = TestDataHelper.generate_name(7)
        return body

    @classmethod
    def create_registration_body_without_password(cls):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body['email'] = TestDataHelper.generate_email(7)
        body['password'] = ''
        body['name'] = TestDataHelper.generate_name(7)
        return body

    @classmethod
    def create_registration_body_without_name(cls):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body['email'] = TestDataHelper.generate_email(7)
        body['password'] = TestDataHelper.generate_password(7)
        body['name'] = ''
        return body

    @classmethod
    def create_change_user_data_body(cls, email, password, name):
        body = TestUserData.CHANGE_USER_DATA_BODY.copy()
        body['email'] = email
        body['password'] = password
        body['name'] = name
        return body

    @classmethod
    def create_order_body(cls):
        body = TestUserData.CREATE_ORDER_BODY.copy()
        body["ingredients"] = []
        body["ingredients"].append("61c0c5a71d1f82001bdaaa71")
        return body

    @classmethod
    def create_empty_order_body(cls):
        body = TestUserData.CREATE_ORDER_BODY.copy()
        body["ingredients"] = []
        return body
