# Владислав Гудков 41-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# 3. Выполнение запроса на получение заказа по треку заказа
def create_and_get_order_status():
    response = sender_stand_request.create_new_order(data.order_body)
    track = response.json()["track"]
    response_track = sender_stand_request.get_order_from_track(track)

    return response_track.status_code

# 4. Проверка, что код ответа равен 200
def test_get_order_from_track_code_200():
    assert create_and_get_order_status() == data.status_success
