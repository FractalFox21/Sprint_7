import pytest
import requests
from data_files.queries import Queries
from data_files.data import Handles
from data_files.generators import register_new_courier_and_return_login_password as new_courier
from data_files.generators import generate_fake_login_pass_name as log_pass_name

@pytest.fixture(scope='function')
def login_and_del_courier():
    login_pass = new_courier()
    response = Queries.post_login_courier(data=login_pass)
    id_courier = response.json()['id']
    yield login_pass
    payload ={"id": id_courier}
    requests.delete(f'{Handles.URL}{Handles.H_COURIER}{id_courier}', json=payload)

@pytest.fixture(scope='function')
def reg_and_del_courier():
    login_pass = log_pass_name()
    yield login_pass
    response = requests.post(f'{Handles.URL}{Handles.H_LOGIN_COURIER}', json=login_pass)
    id_courier = response.json()['id']
    payload ={"id": id_courier}
    requests.delete(f'{Handles.URL}{Handles.H_COURIER}', json=payload)

