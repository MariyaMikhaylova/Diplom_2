import requests

import urls


class BurgerApi:

    @staticmethod
    def create_user(body):
        return requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=body)

    @staticmethod
    def login_user(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_USER_ENDPOINT, json=body)

    @staticmethod
    def change_user_data(body, user_token):
        headers = {'Authorization': user_token}
        return requests.patch(urls.BASE_URL + urls.PATCH_USER_DATA_ENDPOINT, json=body, headers=headers)

    @staticmethod
    def delete_user(user_token):
        headers = {'Authorization': user_token}
        response_delete = requests.delete(f'{urls.BASE_URL + urls.DELETE_USER_ENDPOINT}', headers=headers)
        return response_delete

    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    def create_order_authorized(body, user_token):
        headers = {'Authorization': user_token}
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body, headers=headers)

    @staticmethod
    def get_users_order(user_token):
        headers = {'Authorization': user_token}
        return requests.get(urls.BASE_URL + urls.GET_USERS_ORDER_ENDPOINT, headers=headers)
