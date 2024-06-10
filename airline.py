from nameko.rpc import rpc

import dependencies

class AirlineService:

    name = 'airline_service'

    database = dependencies.Database()

    @rpc
    def get_all_airport(self):
        object = self.database.get_all_airport()
        return object
    
    @rpc
    def get_flight(self, airport_origin_location_code, airport_destination_location_code, date):
        object = self.database.get_flight(airport_origin_location_code, airport_destination_location_code, date)
        return object

    @rpc
    def post_ticket(self, customer_name, flight_code, date):
        object = self.database.post_ticket(customer_name, flight_code, date)
        return object

    @rpc
    def get_ticket(self, customer_name):
        object = self.database.get_ticket(customer_name)
        return object
    