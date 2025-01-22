import allure
import pytest
from data_files.constants import ConstData, ExpectedResp
from data_files.queries import Queries


class TestLoginCourier:

    @allure.title('Позитивный тест авторизации курьера')
    @allure.description('Авторизация зарегистрированного курьера,'
                        ' проверка: запрос возвращает id и статус код 200')
    def test_login_courier_positive_result(self, login_and_del_courier):
        response = Queries.post_login_courier(data=login_and_del_courier)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Негативный тест авторизации, пользователь не найден')
    @allure.description('Авторизация с невалидными данными, логин или пароль некорректные или не были зарегистрированы ранее. '
                        'проверка: запрос возвращает ошибку "Учетная запись не найдена" и статус код 404')
    def test_login_courier_not_found_return_error(self):
        response = Queries.post_login_courier(data=ConstData.data_incorrect)
        assert response.status_code == 404 and ExpectedResp.no_acc in response.text

    @allure.title('Негативный тест авторизации, поле логин или пароль пустое')
    @allure.description('Авторизация с пустым полем логин или пароль. Параметризируются варианты без логина и без пароля. '
                        'Проверка:  запрос возвращает ошибку "Недостаточно данных для входа" и статус код 400')
    @pytest.mark.parametrize('data_without_login_or_password',
                             [ConstData.data_no_login,
                              ConstData.data_no_password])
    def test_login_courier_not_all_data_return_error(self, data_without_login_or_password):
        response = Queries.post_login_courier(data=data_without_login_or_password)
        assert response.status_code == 400 and ExpectedResp.incomplete in response.text