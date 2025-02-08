
class Handles:
    URL = 'http://qa-scooter.praktikum-services.ru'
    H_COURIER = '/api/v1/courier'          #ручка для действия с курьерами
    H_LOGIN_COURIER = '/api/v1/courier/login'     #ручка для логина курьера
    H_ORDERS = '/api/v1/orders'         #ручка для действия с заказами
    H_ACCEPT_ORDER = '/api/v1/orders/accept'    #ручка принять заказ +"id"
    H_GET_ORDER_BY_ID = '/api/v1/orders/track'     #ручка получить заказ по его номеру
