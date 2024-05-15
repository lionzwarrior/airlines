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
    
    @http('POST', '/flight')
    def add_flight(self, request):
        json_file = request.get_json()
        flight = self.airline_rpc.add_flight(json_file["airport_destination"], json_file["capacity"], json_file["price"])
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
