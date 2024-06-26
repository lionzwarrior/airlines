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
    
    @http('GET', '/airport')
    def get_all_airport(self, request):
        object = self.airline_rpc.get_all_airport()
        return 200, json.dumps(object)
    
    @http('GET', '/flight')
    def get_all_flight(self, request):
        object = self.airline_rpc.get_all_flight()
        return 200, json.dumps(object)
    
    @http('GET', '/flight/<string:airport_origin_location_code>/<string:airport_destination_location_code>/<string:date>')
    def get_flight(self, request, airport_origin_location_code, airport_destination_location_code, date):
        object = self.airline_rpc.get_flight(airport_origin_location_code, airport_destination_location_code, date)
        return 200, json.dumps(object)
    
    @http('POST', '/ticket')
    def post_ticket(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.post_ticket(json_file["customer_name"], json_file["flight_code"], json_file["date"])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('GET', '/ticket/<string:customer_name>/<string:date>')
    def get_ticket(self, request, customer_name, date):
        object = self.airline_rpc.get_ticket(customer_name, date)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        