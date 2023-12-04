import pytest
import requests
import allure
from datetime import datetime

from data import Urls
from tests.order_response import OrderResponse


class TestGetUserOrders:

    @allure.title('Test of getting user orders with authorization')
    @allure.description('Test of the endpoint "Получение заказов конкретного пользователя" GET /api/orders.'
                        'Checks that response code is 200 '
                        'that response body contains all required fields'
                        'and that request returns "success": true')
    def test_get_user_orders_with_authorization(self, create_user):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.create_order_url, data=payload, headers=headers)
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 200, f'Instead of code 200 received code {response.status_code}'
        assert response.json().get('success') is True, 'Field "success" is not True in the response body'
        order_response = OrderResponse(response.json())
        order_response.check_orders_field()
        order_response.check_total_field()
        order_response.check_total_today_field()
        orders_data = response.json().get('orders')[0]
        order_response.check_order_fields(orders_data)

    @allure.title('Test of getting no more that 50 last user orders with authorization')
    @allure.description('Test of the endpoint "Получение заказов конкретного пользователя" GET /api/orders.'
                        'Parametrized test that checks that response contains no more than 50 last user orders'
                        'that response code is 200 '
                        'and that request returns "success": true')
    @pytest.mark.parametrize('create_n_orders, orders_to_receive', [
        (49, 49),
        (50, 50),
        (51, 50)
    ], indirect=['create_n_orders'])
    def test_get_no_more_than_fifty_last_user_orders_with_authorization(self, create_user,
                                                                        create_n_orders, orders_to_receive):
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 200, f'Instead of code 200 received code {response.status_code}'
        assert response.json().get('success') is True, 'Field "success" is not True in the response body'
        orders = response.json().get('orders')
        assert len(orders) == orders_to_receive, f'Number of last user orders in response is not {orders_to_receive}'

    @allure.title('Test of sorting user orders with authorization')
    @allure.description('Test of the endpoint "Получение заказов конкретного пользователя" GET /api/orders.'
                        'Checks that response contains user orders sorted by Update time ascending'
                        'that response code is 200 '
                        'and that request returns "success": true')
    def test_sorting_user_orders_with_authorization(self, create_user, create_three_orders):
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 200, f'Instead of code 200 received code {response.status_code}'
        assert response.json().get('success') is True, 'Field "success" is not True in the response body'
        orders = response.json().get('orders')
        sorted_orders = sorted(orders, key=lambda x: datetime.strptime(x['updatedAt'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                               reverse=False)
        assert orders == sorted_orders, 'User orders are not sorted by update time in descending order'

    @allure.title('Test of failed attempt to get user orders without authorization')
    @allure.description('Negative test of the endpoint "Получение заказов конкретного пользователя" GET /api/orders.'
                        'Checks that response code is 401 '
                        'that response body contains all required fields'
                        'and that request returns "success": false')
    def test_get_user_orders_without_authorization_failed(self, create_user):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.create_order_url, data=payload, headers=headers)
        headers = {}
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 401, f'Instead of code 401 received code {response.status_code}'
        assert response.json().get('success') is False, 'Field "success" is not False in the response body'
        assert response.json()['message'] == 'You should be authorised', f'Error message contains wrong text'
