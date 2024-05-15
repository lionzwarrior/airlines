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
    def edit_reservation(self, id, ticket_id):
        reservation = self.database.edit_reservation(id, ticket_id)
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
    def edit_ticket(self, id, flight_type, start_datetime, end_datetime):
        ticket = self.database.edit_ticket(id, flight_type, start_datetime, end_datetime)
        return ticket
    
    @rpc
    def delete_ticket(self, id):
        ticket = self.database.delete_ticket(id)
        return ticket
    
    @rpc
    def check_ticket(self, id):
        ticket = self.database.check_ticket(id)
        return ticket
    
    @rpc
    def add_flight(self, class_type, airport_origin, airport_destination, capacity, price):
        flight = self.database.add_flight(class_type, airport_origin, airport_destination, capacity, price)
        return flight
    
    @rpc
    def get_all_flights(self):
        flights = self.database.get_all_flights()
        return flights

    @rpc
    def get_flight(self, id):
        flight = self.database.get_flight(id)
        return flight
    
    @rpc
    def edit_flight(self, id, class_type, airport_origin, airport_destination, capacity, price):
        flight = self.database.edit_flight(id, class_type, airport_origin, airport_destination, capacity, price)
        return flight
    
    @rpc
    def delete_flight(self, id):
        flight = self.database.delete_flight(id)
        return flight

    @rpc
    def add_class(self, name):
        class_obj = self.database.add_class(name)
        return class_obj
    
    @rpc
    def get_all_class(self):
        class_obj = self.database.get_all_class()
        return class_obj
    
    @rpc
    def get_class(self, id):
        class_obj = self.database.get_class(id)
        return class_obj
    
    @rpc
    def edit_class(self, id, name):
        class_obj = self.database.edit_class(id, name)
        return class_obj
    
    @rpc
    def delete_class(self, id):
        class_obj = self.database.delete_class(id)
        return class_obj

    @rpc
    def add_airport(self, name):
        airport = self.database.add_airport(name)
        return airport
    
    @rpc
    def get_all_airport(self):
        airport = self.database.get_all_airport()
        return airport
    
    @rpc
    def get_airport(self, id):
        airport = self.database.get_airport(id)
        return airport
    
    @rpc
    def edit_airport(self, id, name):
        airport = self.database.edit_airport(id, name)
        return airport
    
    @rpc
    def delete_airport(self, id):
        airport = self.database.delete_airport(id)
        return airport
