import configuration
import requests
import data

# 1. Выполнение запроса на создание заказа:
def create_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
	                     json = order_body,
	                     headers = data.headers)

# 2. Получение заказа по номеру трекера
def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER + str(track),
	                    headers = data.headers)