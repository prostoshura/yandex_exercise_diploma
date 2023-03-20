import url  # импортируем данные из url
import sender_stand_request  # импортируем данные из вкладки с запросом


def get_get_request_an_order(track):
    # копирование словаря с телом запроса из url, чтобы не потерять данные в исходном словаре
    current_order_request = sender_stand_request.get_request_an_order()
    # изменение значения в поле track
    current_order_request["track"] = track
    # Возвращается новый словарь с нужным значением track
    return current_order_request


def positive_assert(order_track):
    # В переменную post_new_client_kit сохраняется обновленное тело запроса
    get_request_an_order = get_get_request_an_order(order_track)
    # В переменную user_response сохраняется результат запроса на создание набора
    user_response = sender_stand_request.get_request_an_order()


# Проверяется, что код ответа равен 200
    assert user_response.status_code == 200
    # Проверяется, что в ответе значение track соответствует track в запросе
    assert user_response.json()["track"] == order_track
    # Проверяется полный ответ на запрос
    print(user_response.json())


# Проверка успешности запроса заказа по номеру трека:
def test_create_new_order_request_by_track():
    positive_assert(710664)
