import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:

    name = 'gateway'

    airline_rpc = RpcProxy('airline_service')
    
    @http('POST', '/ticket')
    def add_ticket(self, request, flight_id):
        json_file = request.get_json()
        ticket = self.airline_rpc.add_ticket(json_file["flight_id"])
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

    @http('DELETE', '/ticket/<int:id>')
    def delete_ticket(self, request, id):
        ticket = self.airline_rpc.delete_ticket(id)
        if ticket["status"] == "success":
            return 200, json.dumps(ticket)
        elif ticket["status"] == "not_found":
            return 404, json.dumps(ticket)
        else:
            return 400, json.dumps(ticket)
