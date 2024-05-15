from nameko.rpc import rpc

import dependencies

class AirLineService:

    name = 'airline_service'

    database = dependencies.Database()

    @rpc
    def add_ticket(self, flight_id):
        ticket = self.database.add_ticket(flight_id)
        return ticket
    
    @rpc
    def get_all_tickets(self):
        tickets = self.database.get_all_tickets()
        return tickets
    
    @rpc
    def get_ticket(self, id):
        ticket = self.database.get_ticket(id)
        return ticket
    
    @rpc
    def delete_ticket(self, id):
        ticket = self.database.delete_ticket(id)
        return ticket
