from nameko.rpc import rpc

import dependencies

class AirLineService:

    name = 'airline_service'

    database = dependencies.Database()

    @rpc
    def add_reservation(self, ticket_id):
        reservation = self.database.add_reservation(ticket_id)
        return reservation
    
    @rpc
    def get_all_reservations(self):
        reservations = self.database.get_all_reservations()
        return reservations
    
    @rpc
    def get_reservation(self, id):
        reservation = self.database.get_reservation(id)
        return reservation
    
    @rpc
    def delete_reservation(self, id):
        reservation = self.database.delete_reservation(id)
        return reservation
    
    @rpc
    def add_ticket(self, flight_type, start_datetime, end_datetime):
        ticket = self.database.add_ticket(flight_type, start_datetime, end_datetime)
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
    def add_flight(self, airport_origin, airport_destination, capacity, price):
        ticket = self.database.add_flight(airport_origin, airport_destination, capacity, price)
        return ticket
    
    @rpc
    def get_all_flights(self):
        tickets = self.database.get_all_flights()
        return tickets

    @rpc
    def get_flight(self, id):
        ticket = self.database.get_flight(id)
        return ticket
