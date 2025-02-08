import requests
from data_files.data import Handles


class Queries:

    @staticmethod
    def post_create_courier(data=None):
        url = f"{Handles.URL}{Handles.H_COURIER}"
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def post_login_courier(data=None):
        url = f"{Handles.URL}{Handles.H_LOGIN_COURIER}"
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        return response

    @staticmethod
    def get_orders(params=None):
        url = f"{Handles.URL}{Handles.H_ORDERS}"
        response = requests.get(url, params=params)
        return response

    @staticmethod
    def post_orders(data=None):
        url = f"{Handles.URL}{Handles.H_ORDERS}"
        response = requests.post(url, data=data, headers = {'Content-Type': 'application/json'})
        return response


