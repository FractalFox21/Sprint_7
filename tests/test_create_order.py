import pytest
import json
import allure
from data_files.constants import ConstData
from data_files.queries import Queries

class TestCreateOrder:

    @allure.title('Позитивный тест создания заказа')
    @allure.description('При создании заказа параметризируется цвет:- черный, серый, оба цвета и пустое поле. '
                        'Проверка: статус код 201 и ответ содержит слово "track".')
    @pytest.mark.parametrize('order_data',
                             [{"color": ["BLACK"]},
                              {"color": ["GREY"]},
                              {"color": ["BLACK", "GREY"]},
                              {"color": [""]}])
    def test_create_order_param_color_order_created(self, order_data):
        ConstData.data_order.update(order_data)
        order_data = json.dumps(ConstData.data_order)
        response = Queries.post_orders(data=order_data)
        assert response.status_code == 201 and ('track' in response.json())