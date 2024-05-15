import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:

    name = 'gateway'

    airline_rpc = RpcProxy('airline_service')
    
    @http('POST', '/reservation')
    def add_reservation(self, request, ticket_id):
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
    def add_ticket(self, request, ticket_type, start_datetime, end_datetime):
        json_file = request.get_json()
        reservation = self.airline_rpc.add_reservation(json_file["ticket_type"], json_file["start_datetime"], json_file["end_datetime"])
        if reservation["status"] == "success":
            return 201, json.dumps(reservation)
        else:
            return 400, json.dumps(reservation)

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
