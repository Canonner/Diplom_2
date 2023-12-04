class OrderResponse:

    def __init__(self, response_json):
        self.response_json = response_json
        self.orders_data = response_json.get('orders', [])

    def check_orders_field(self):
        assert 'orders' in self.response_json, 'Field "orders" is missing in the response body'


    def check_total_field(self):
        assert 'total' in self.response_json, 'Field "total" is missing in the response body'

    def check_total_today_field(self):
        assert 'totalToday' in self.response_json, 'Field "totalToday" is missing in the response body'

    def check_order_fields(self, order_data):
        assert '_id' in order_data, 'Field "_id" is missing in the "orders" field of the response body'
        assert 'ingredients' in order_data, 'Field "ingredients" is missing in the "orders" field of the response body'
        assert 'status' in order_data, 'Field "status" is missing in the "orders" field of the response body'
        assert 'createdAt' in order_data, 'Field "createdAt" is missing in the "orders" field of the response body'
        assert 'updatedAt' in order_data, 'Field "updatedAt" is missing in the "orders" field of the response body'
        assert 'number' in order_data, 'Field "number" is missing in the "orders" field of the response body'
