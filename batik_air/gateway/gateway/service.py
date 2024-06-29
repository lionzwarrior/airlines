import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from werkzeug.wrappers import Response

class GatewayService:

    name = 'gateway'

    airline_rpc = RpcProxy('batik_air_service')
    
    def add_cors_headers(self, response):
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Content-type": "application/json"
        }
        response.headers.extend(headers)
        return response

    @http('OPTIONS', '/<path:catch_all>')
    def options(self, request, catch_all):
        response = Response('', status=200)
        return self.add_cors_headers(response)
    
    @http('GET', '/airport')
    def get_all_airport(self, request):
        object = self.airline_rpc.get_all_airport()
        response = Response(json.dumps(object), status=200, mimetype='application/json')
        return self.add_cors_headers(response)
    
    @http('GET', '/flight')
    def get_all_flight(self, request):
        object = self.airline_rpc.get_all_flight()
        response = Response(json.dumps(object), status=200, mimetype='application/json')
        return self.add_cors_headers(response)
    
    @http('GET', '/flight/<string:airport_origin_location_code>/<string:airport_destination_location_code>/<string:date>')
    def get_flight(self, request, airport_origin_location_code, airport_destination_location_code, date):
        object = self.airline_rpc.get_flight(airport_origin_location_code, airport_destination_location_code, date)
        response = Response(json.dumps(object), status=200, mimetype='application/json')
        return self.add_cors_headers(response)
    
    @http('POST', '/ticket')
    def post_ticket(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.post_ticket(json_file["customer_name"], json_file["flight_code"], json_file["date"], json_file['class_name'])
        status = 201 if object["status"] == "success" else 400
        response = Response(json.dumps(object), status=status, mimetype='application/json')
        return self.add_cors_headers(response)
    
    @http('GET', '/ticket/<string:customer_name>')
    def get_ticket(self, request, customer_name):
        object = self.airline_rpc.get_ticket(customer_name)
        response = Response(json.dumps(object), status=200, mimetype='application/json')
        return self.add_cors_headers(response)
        