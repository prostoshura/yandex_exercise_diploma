# Шаги автотеста:
# Выполнить запрос на создание заказа.
# Сохранить номер трека заказа.
# Выполнить запрос на получение заказа по треку заказа.
# Проверить, что код ответа равен 200.


import body  # импортируем данные из body
import url  # импортируем данные из url
import requests  # импортируем библиотеку requests


def post_new_order(order_body):  # Функция для изменения значения в параметре body в теле запроса на создание заказа
    return requests.post(url.url+url.Make_an_order_path,
                         json=body.Make_an_order,  # указываем тело запроса на создание заказа
                         headers=body.headers)  # указываем заголовок запроса на создание заказа


# В переменную response сохраняется результат запроса на создание заказа
response = post_new_order(body.Make_an_order)
# Проверяется полный ответ на запрос
print(response.json())


def get_new_order_track():  # Запрос на создание заказа
    order_body = body.Make_an_order
    resp_order = post_new_order(body.Make_an_order)
    return resp_order.json()["track"]  # Возврат запроса, запомнить трек Заказа


def get_request_an_order():  # Запрос на поиск заказа по его трек номеру
    return requests.get(url.url+url.Get_an_order_number+get_new_order_track()["track"])


print(response.json())