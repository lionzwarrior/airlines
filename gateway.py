import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:

    name = 'gateway'

    airline_rpc = RpcProxy('airline_service')
    
    @http('POST', '/reservation')
    def add_reservation(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_reservation(json_file["customer_name"], json_file["ticket_id"], json_file["chair_number_id"], json_file["gateway_id"])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('GET', '/reservation')
    def get_all_reservations(self, request):
        object = self.airline_rpc.get_all_reservations()
        return 200, json.dumps(object)

    @http('GET', '/reservation/<int:id>')
    def get_reservation(self, request, id):
        object = self.airline_rpc.get_reservation(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('PUT', '/reservation/<int:id>')
    def edit_reservation(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_reservation(id, json_file["customer_name"], json_file["ticket_id"], json_file["chair_number_id"], json_file["gateway_id"])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('DELETE', '/reservation/<int:id>')
    def delete_reservation(self, request, id):
        object = self.airline_rpc.delete_reservation(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('POST', '/ticket')
    def add_ticket(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_ticket(json_file["flight_id"], json_file["date"], json_file["start_time"], json_file["finish_time"])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('GET', '/ticket')
    def get_all_tickets(self, request):
        object = self.airline_rpc.get_all_tickets()
        return 200, json.dumps(object)

    @http('GET', '/ticket/<int:id>')
    def get_ticket(self, request, id):
        object = self.airline_rpc.get_ticket(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/ticket/<int:id>')
    def edit_ticket(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_ticket(id, json_file["flight_id"], json_file["date"], json_file["start_time"], json_file["finish_time"])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('DELETE', '/ticket/<int:id>')
    def delete_ticket(self, request, id):
        object = self.airline_rpc.delete_ticket(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('POST', '/flight')
    def add_flight(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_flight(json_file["airline_id"], json_file['class_id'], json_file["airport_origin_id"], json_file["airport_destination_id"], json_file["capacity"], json_file['weight_limit'], json_file["price"])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('GET', '/flight')
    def get_all_flights(self, request):
        object = self.airline_rpc.get_all_flights()
        return 200, json.dumps(object)

    @http('GET', '/flight/<int:id>')
    def get_flight(self, request, id):
        object = self.airline_rpc.get_flight(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/flight/<int:id>')
    def edit_flight(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_flight(id, json_file["airline_id"], json_file['class_id'], json_file["airport_origin_id"], json_file["airport_destination_id"], json_file["capacity"], json_file['weight_limit'], json_file["price"])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/flight/<int:id>')
    def delete_flight(self, request, id):
        object = self.airline_rpc.delete_flight(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('POST', '/class')
    def add_class(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_class(json_file['name'])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('GET', '/class')
    def get_all_class(self, request):
        object = self.airline_rpc.get_all_class()
        return 200, json.dumps(object)
    
    @http('GET', '/class/<int:id>')
    def get_class(self, request, id):
        object = self.airline_rpc.get_class(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/class/<int:id>')
    def edit_class(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_class(id, json_file['name'])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/class/<int:id>')
    def delete_class(self, request, id):
        object = self.airline_rpc.delete_class(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('POST', '/airport')
    def add_airport(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_airport(json_file['name'])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('GET', '/airport')
    def get_all_airport(self, request):
        object = self.airline_rpc.get_all_airport()
        return 200, json.dumps(object)
    
    @http('GET', '/airport/<int:id>')
    def get_airport(self, request, id):
        object = self.airline_rpc.get_airport(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/airport/<int:id>')
    def edit_airport(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_airport(id, json_file['name'])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/airport/<int:id>')
    def delete_airport(self, request, id):
        object = self.airline_rpc.delete_airport(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('POST', '/airline')
    def add_airline(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_airline(json_file['name'])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('GET', '/airline')
    def get_all_airline(self, request):
        object = self.airline_rpc.get_all_airline()
        return 200, json.dumps(object)
    
    @http('GET', '/airline/<int:id>')
    def get_airline(self, request, id):
        object = self.airline_rpc.get_airline(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/airline/<int:id>')
    def edit_airline(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_airline(id, json_file['name'])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/airline/<int:id>')
    def delete_airline(self, request, id):
        object = self.airline_rpc.delete_airline(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('POST', '/chair_number')
    def add_chair_number(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_chair_number(json_file['name'], json_file['flight_id'])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('GET', '/chair_number')
    def get_all_chair_number(self, request):
        object = self.airline_rpc.get_all_chair_number()
        return 200, json.dumps(object)
    
    @http('GET', '/chair_number/<int:id>')
    def get_chair_number(self, request, id):
        object = self.airline_rpc.get_chair_number(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/chair_number/<int:id>')
    def edit_chair_number(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_chair_number(id, json_file['name'], json_file['flight_id'])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/chair_number/<int:id>')
    def delete_chair_number(self, request, id):
        object = self.airline_rpc.delete_chair_number(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)

    @http('POST', '/gateway')
    def add_gateway(self, request):
        json_file = request.get_json()
        object = self.airline_rpc.add_gateway(json_file['name'], json_file['airport_id'])
        if object["status"] == "success":
            return 201, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('GET', '/gateway')
    def get_all_gateway(self, request):
        object = self.airline_rpc.get_all_gateway()
        return 200, json.dumps(object)
    
    @http('GET', '/gateway/<int:id>')
    def get_gateway(self, request, id):
        object = self.airline_rpc.get_gateway(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('PUT', '/gateway/<int:id>')
    def edit_gateway(self, request, id):
        json_file = request.get_json()
        object = self.airline_rpc.edit_gateway(id, json_file['name'], json_file['airport_id'])
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
        
    @http('DELETE', '/gateway/<int:id>')
    def delete_gateway(self, request, id):
        object = self.airline_rpc.delete_gateway(id)
        if object["status"] == "success":
            return 200, json.dumps(object)
        elif object["status"] == "not_found":
            return 404, json.dumps(object)
        else:
            return 400, json.dumps(object)
