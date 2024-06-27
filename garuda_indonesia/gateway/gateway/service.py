import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:

    name = 'gateway'
    
    header = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE",
        "Access-Control-Allow-Headers": "*",
        "Content-type": "application/json"
    }

    airline_rpc = RpcProxy('batik_air_service')
    
    def add_cors_headers(self, response):
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Content-type": "application/json"
        }
        response.headers.update(headers)
        return response

    @http('OPTIONS', '/<path:catch_all>')
    def options(self, request, catch_all):
        return self.add_cors_headers((200, ''))
    
    @http('GET', '/airport')
    def get_all_airport(self, request):
        object = self.airline_rpc.get_all_airport()
        response = 200, json.dumps(object)
        return self.add_cors_headers(response)
    
    @http('GET', '/flight')
    def get_all_flight(self, request):
        object = self.airline_rpc.get_all_flight()
        response = 200, json.dumps(object)
        return self.add_cors_headers(response)
    
    @http('GET', '/flight/<string:airport_origin_location_code>/<string:airport_destination_location_code>/<string:date>')
    def get_flight(self, request, airport_origin_location_code, airport_destination_location_code, date):
        object = self.airline_rpc.get_flight(airport_origin_location_code, airport_destination_location_code, date)
        response = 200, json.dumps(object)
        return self.add_cors_headers(response)
    
    @http('POST', '/ticket')
    def post_ticket(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.post_ticket(json_file["customer_name"], json_file["flight_code"], json_file["date"])
        response = (201 if object["status"] == "success" else 400), json.dumps(object)
        return self.add_cors_headers(response)
        
    @http('GET', '/ticket/<string:customer_name>/<string:date>')
    def get_ticket(self, request, customer_name, date):
        object = self.airline_rpc.get_ticket(customer_name, date)
        if object["status"] == "success":
            response = 200, json.dumps(object)
        elif object["status"] == "not_found":
            response = 404, json.dumps(object)
        else:
            response = 400, json.dumps(object)
        return self.add_cors_headers(response)
        