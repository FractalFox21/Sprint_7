

class ConstData:

    data_incorrect = {      #данные для авторизации, которые содаржат ошибку или несуществуют
        "login": "validlogin",
        "password": "123sffsv"}
    data_no_login = {           #данные для авторизации без логина
        "login": "",
        "password": "123sffsv" }
    data_no_password = {        #данные для авторизации без пароля
        "login": "validlogin",
        "password": "" }

    data_order = {      #данные для заказа
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Otradnaya str, 1",
    "metroStation": 2,
    "phone": "+78888888888",
    "rentTime": 2,
    "deliveryDate": "2025-02-20",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]}



class ExpectedResp:

    ok = '{"ok":true}'
    no_acc = 'Учетная запись не найдена'
    incomplete = 'Недостаточно данных для входа'
    occupied = 'Этот логин уже используется'
    no_full = 'Недостаточно данных для создания учетной записи'