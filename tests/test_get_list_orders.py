import allure
from data_files.queries import Queries

class TestListOrder:
    @allure.title('Запрос отображения списка заказов')
    @allure.description('Запрос выводит список заказов '
                        'Проверка: статус код 200 и текст в ответе  "orders".')
    def test_response_contains_list_of_order(self):
        params = {"limit": 10}
        response = Queries.get_orders(params=params)
        assert response.status_code == 200 and 'orders' in response.json()