import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:

    name = 'gateway'

    airline_rpc = RpcProxy('airline_service')
    
    @http('POST', '/reservation')
    def add_reservation(self, request):
        json_file = request.get_json()
        reservation = self.airline_rpc.add_reservation(json_file["ticket_id"])
        if reservation["status"] == "success":
            return 201, json.dumps(reservation)
        else:
            return 400, json.dumps(reservation)

    @http('GET', '/reservation')
    def get_all_reservations(self, request):
        reservations = self.airline_rpc.get_all_reservations()
        return 200, json.dumps(reservations)

    @http('GET', '/reservation/<int:id>')
    def get_reservation(self, request, id):
        reservation = self.airline_rpc.get_reservation(id)
        if reservation["status"] == "success":
            return 200, json.dumps(reservation)
        elif reservation["status"] == "not_found":
            return 404, json.dumps(reservation)
        else:
            return 400, json.dumps(reservation)

    @http('PUT', '/reservation/<int:id>')
    def edit_reservation(self, request, id):
        json_file = request.get_json()
        reservation = self.airline_rpc.edit_reservation(id, json_file['ticket_id'])
        if reservation["status"] == "success":
            return 200, json.dumps(reservation)
        elif reservation["status"] == "not_found":
            return 404, json.dumps(reservation)
        else:
            return 400, json.dumps(reservation)

    @http('DELETE', '/reservation/<int:id>')
    def delete_reservation(self, request, id):
        reservation = self.airline_rpc.delete_reservation(id)
        if reservation["status"] == "success":
            return 200, json.dumps(reservation)
        elif reservation["status"] == "not_found":
            return 404, json.dumps(reservation)
        else:
            return 400, json.dumps(reservation)
        
    @http('POST', '/ticket')
    def add_ticket(self, request):
        json_file = request.get_json()
        ticket = self.airline_rpc.add_ticket(json_file["flight_type"], json_file["start_datetime"], json_file["end_datetime"])
        if ticket["status"] == "success":
            return 201, json.dumps(ticket)
        else:
            return 400, json.dumps(ticket)

    @http('GET', '/ticket')
    def get_all_tickets(self, request):
        tickets = self.airline_rpc.get_all_tickets()
        return 200, json.dumps(tickets)

    @http('GET', '/ticket/<int:id>')
    def get_ticket(self, request, id):
        ticket = self.airline_rpc.get_ticket(id)
        if ticket["status"] == "success":
            return 200, json.dumps(ticket)
        elif ticket["status"] == "not_found":
            return 404, json.dumps(ticket)
        else:
            return 400, json.dumps(ticket)
        
    @http('PUT', '/ticket/<int:id>')
    def edit_ticket(self, request, id):
        json_file = request.get_json()
        ticket = self.airline_rpc.edit_ticket(id, json_file['flight_type'], json_file['start_datetime'], json_file['end_datetime'])
        if ticket["status"] == "success":
            return 200, json.dumps(ticket)
        elif ticket["status"] == "not_found":
            return 404, json.dumps(ticket)
        else:
            return 400, json.dumps(ticket)

    @http('DELETE', '/ticket/<int:id>')
    def delete_ticket(self, request, id):
        ticket = self.airline_rpc.delete_ticket(id)
        if ticket["status"] == "success":
            return 200, json.dumps(ticket)
        elif ticket["status"] == "not_found":
            return 404, json.dumps(ticket)
        else:
            return 400, json.dumps(ticket)

    @http('POST', '/flight')
    def add_flight(self, request):
        json_file = request.get_json()
        flight = self.airline_rpc.add_flight(json_file['class_type'], json_file["airport_origin"], json_file["airport_destination"], json_file["capacity"], json_file['weight_limit'], json_file["price"])
        if flight["status"] == "success":
            return 201, json.dumps(flight)
        else:
            return 400, json.dumps(flight)

    @http('GET', '/flight')
    def get_all_flights(self, request):
        flights = self.airline_rpc.get_all_flights()
        return 200, json.dumps(flights)

    @http('GET', '/flight/<int:id>')
    def get_flight(self, request, id):
        flight = self.airline_rpc.get_flight(id)
        if flight["status"] == "success":
            return 200, json.dumps(flight)
        elif flight["status"] == "not_found":
            return 404, json.dumps(flight)
        else:
            return 400, json.dumps(flight)
        
    @http('PUT', '/flight/<int:id>')
    def edit_flight(self, request, id):
        json_file = request.get_json()
        flight = self.airline_rpc.edit_flight(id, json_file['class_type'], json_file['airport_origin'], json_file['airport_destination'], json_file['capacity'], json_file['weight_limit'], json_file['price'])
        if flight["status"] == "success":
            return 200, json.dumps(flight)
        elif flight["status"] == "not_found":
            return 404, json.dumps(flight)
        else:
            return 400, json.dumps(flight)
        
    @http('DELETE', '/flight/<int:id>')
    def delete_flight(self, request, id):
        flight = self.airline_rpc.delete_flight(id)
        if flight["status"] == "success":
            return 200, json.dumps(flight)
        elif flight["status"] == "not_found":
            return 404, json.dumps(flight)
        else:
            return 400, json.dumps(flight)
        
    @http('POST', '/class')
    def add_class(self, request):
        json_file = request.get_json()
        class_obj = self.airline_rpc.add_class(json_file['name'])
        if class_obj["status"] == "success":
            return 201, json.dumps(class_obj)
        else:
            return 400, json.dumps(class_obj)

    @http('GET', '/class')
    def get_all_class(self, request):
        class_obj = self.airline_rpc.get_all_class()
        return 200, json.dumps(class_obj)
    
    @http('GET', '/class/<int:id>')
    def get_class(self, request, id):
        class_obj = self.airline_rpc.get_class(id)
        if class_obj["status"] == "success":
            return 200, json.dumps(class_obj)
        elif class_obj["status"] == "not_found":
            return 404, json.dumps(class_obj)
        else:
            return 400, json.dumps(class_obj)
        
    @http('PUT', '/class/<int:id>')
    def edit_class(self, request, id):
        json_file = request.get_json()
        class_obj = self.airline_rpc.edit_class(id, json_file['name'])
        if class_obj["status"] == "success":
            return 200, json.dumps(class_obj)
        elif class_obj["status"] == "not_found":
            return 404, json.dumps(class_obj)
        else:
            return 400, json.dumps(class_obj)
        
    @http('DELETE', '/class/<int:id>')
    def delete_class(self, request, id):
        class_obj = self.airline_rpc.delete_class(id)
        if class_obj["status"] == "success":
            return 200, json.dumps(class_obj)
        elif class_obj["status"] == "not_found":
            return 404, json.dumps(class_obj)
        else:
            return 400, json.dumps(class_obj)

    @http('POST', '/airport')
    def add_airport(self, request):
        json_file = request.get_json()
        airport = self.airline_rpc.add_airport(json_file['name'])
        if airport["status"] == "success":
            return 201, json.dumps(airport)
        else:
            return 400, json.dumps(airport)
        
    @http('GET', '/airport')
    def get_all_airport(self, request):
        airport = self.airline_rpc.get_all_airport()
        return 200, json.dumps(airport)
    
    @http('GET', '/airport/<int:id>')
    def get_airport(self, request, id):
        airport = self.airline_rpc.get_airport(id)
        if airport["status"] == "success":
            return 200, json.dumps(airport)
        elif airport["status"] == "not_found":
            return 404, json.dumps(airport)
        else:
            return 400, json.dumps(airport)
        
    @http('PUT', '/airport/<int:id>')
    def edit_airport(self, request, id):
        json_file = request.get_json()
        airport = self.airline_rpc.edit_airport(id, json_file['name'])
        if airport["status"] == "success":
            return 200, json.dumps(airport)
        elif airport["status"] == "not_found":
            return 404, json.dumps(airport)
        else:
            return 400, json.dumps(airport)
        
    @http('DELETE', '/airport/<int:id>')
    def delete_airport(self, request, id):
        airport = self.airline_rpc.delete_airport(id)
        if airport["status"] == "success":
            return 200, json.dumps(airport)
        elif airport["status"] == "not_found":
            return 404, json.dumps(airport)
        else:
            return 400, json.dumps(airport)
