import allure
from data_files.queries import Queries
from data_files.constants import ExpectedResp
from data_files.generators import generate_user_data_no_password as gen_no_pass
from data_files.generators import generate_user_data_no_login as gen_no_login


class TestCreateCourier:

    @allure.title('Позитивный тест создания нового курьера.')
    @allure.description('Регистрация нового курьера'
                        'Проверка: статус код 201 и текст ответа "{"ok":true}"')
    def test_create_courier_positive_result(self, reg_and_del_courier):
        response = Queries.post_create_courier(data=reg_and_del_courier)
        assert response.status_code == 201 and ExpectedResp.ok == response.text


    @allure.title('Негативный тест, создание дубликата')
    @allure.description('Попытка создать второго курьера с теми же данными.'
                        'Проверка: статус код 409 и ошибка "Этот логин уже используется"')
    def test_request_with_duplicate_login_return_error(self, login_and_del_courier):
        response = Queries.post_create_courier(data=login_and_del_courier)
        assert response.status_code == 409 and ExpectedResp.occupied in response.text


    @allure.title('Негативный тест создания нового курьера с пустым полем "логин"')
    @allure.description('Попытка создать курьера, с пустым полем "логин", '
                        'Проверка: статус код 400 и ошибка "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_login_return_error(self):
        response = Queries.post_create_courier(data=gen_no_login())
        assert response.status_code == 400 and ExpectedResp.no_full in response.text

    @allure.title('Негативный тест создания нового курьера с пустым полем "пароль"')
    @allure.description('Попытка создать курьера, с пустым полем "пароль". '
                        'Проверка: статус код 400 и ошибка "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password_return_error(self):
        response = Queries.post_create_courier(data=gen_no_pass())
        assert response.status_code == 400 and ExpectedResp.no_full in response.text
