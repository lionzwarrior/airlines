from nameko.rpc import rpc

import dependencies

class AirLineService:

    name = 'airline_service'

    database = dependencies.Database()

    @rpc
    def add_reservation(self, customer_name, ticket_id, chair_number_id, gateway_id):
        object = self.database.add_reservation(customer_name, ticket_id, chair_number_id, gateway_id)
        return object
    
    @rpc
    def get_all_reservations(self):
        object = self.database.get_all_reservations()
        return object
    
    @rpc
    def get_reservation(self, id):
        object = self.database.get_reservation(id)
        return object
    
    @rpc
    def edit_reservation(self, id, customer_name, ticket_id, chair_number_id, gateway_id):
        object = self.database.edit_reservation(id, customer_name, ticket_id, chair_number_id, gateway_id)
        return object
    
    @rpc
    def delete_reservation(self, id):
        object = self.database.delete_reservation(id)
        return object
    
    @rpc
    def add_ticket(self, flight_id, date, start_time, finish_time):
        object = self.database.add_ticket(flight_id, date, start_time, finish_time)
        return object
    
    @rpc
    def get_all_tickets(self):
        object = self.database.get_all_tickets()
        return object

    @rpc
    def get_ticket(self, id):
        object = self.database.get_ticket(id)
        return object
    
    @rpc
    def edit_ticket(self, id, flight_id, date, start_time, finish_time):
        object = self.database.edit_ticket(id, flight_id, date, start_time, finish_time)
        return object
    
    @rpc
    def delete_ticket(self, id):
        object = self.database.delete_ticket(id)
        return object
    
    @rpc
    def add_flight(self, airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price):
        object = self.database.add_flight(airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price)
        return object
    
    @rpc
    def get_all_flights(self):
        object = self.database.get_all_flights()
        return object

    @rpc
    def get_flight(self, id):
        object = self.database.get_flight(id)
        return object
    
    @rpc
    def edit_flight(self, id, airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price):
        object = self.database.edit_flight(id, airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price)
        return object
    
    @rpc
    def delete_flight(self, id):
        object = self.database.delete_flight(id)
        return object

    @rpc
    def add_class(self, name):
        object = self.database.add_class(name)
        return object
    
    @rpc
    def get_all_class(self):
        object = self.database.get_all_class()
        return object
    
    @rpc
    def get_class(self, id):
        object = self.database.get_class(id)
        return object
    
    @rpc
    def edit_class(self, id, name):
        object = self.database.edit_class(id, name)
        return object
    
    @rpc
    def delete_class(self, id):
        object = self.database.delete_class(id)
        return object

    @rpc
    def add_airport(self, name):
        object = self.database.add_airport(name)
        return object
    
    @rpc
    def get_all_airport(self):
        object = self.database.get_all_airport()
        return object
    
    @rpc
    def get_airport(self, id):
        object = self.database.get_airport(id)
        return object
    
    @rpc
    def edit_airport(self, id, name):
        object = self.database.edit_airport(id, name)
        return object
    
    @rpc
    def delete_airport(self, id):
        object = self.database.delete_airport(id)
        return object
    
    @rpc
    def add_airline(self, name):
        object = self.database.add_airline(name)
        return object
    
    @rpc
    def get_all_airline(self):
        object = self.database.get_all_airline()
        return object
    
    @rpc
    def get_airline(self, id):
        object = self.database.get_airline(id)
        return object
    
    @rpc
    def edit_airline(self, id, name):
        object = self.database.edit_airline(id, name)
        return object
    
    @rpc
    def delete_airline(self, id):
        object = self.database.delete_airline(id)
        return object
    
    @rpc
    def add_chair_number(self, name, flight_id):
        object = self.database.add_chair_number(name, flight_id)
        return object
    
    @rpc
    def get_all_chair_number(self):
        object = self.database.get_all_chair_number()
        return object
    
    @rpc
    def get_chair_number(self, id):
        object = self.database.get_chair_number(id)
        return object
    
    @rpc
    def edit_chair_number(self, id, name, flight_id):
        object = self.database.edit_chair_number(id, name, flight_id)
        return object
    
    @rpc
    def delete_chair_number(self, id):
        object = self.database.delete_chair_number(id)
        return object
    
    @rpc
    def add_gateway(self, name, airport_id):
        object = self.database.add_gateway(name, airport_id)
        return object
    
    @rpc
    def get_all_gateway(self):
        object = self.database.get_all_gateway()
        return object
    
    @rpc
    def get_gateway(self, id):
        object = self.database.get_gateway(id)
        return object
    
    @rpc
    def edit_gateway(self, id, name, airport_id):
        object = self.database.edit_gateway(id, name, airport_id)
        return object
    
    @rpc
    def delete_gateway(self, id):
        object = self.database.delete_gateway(id)
        return object
