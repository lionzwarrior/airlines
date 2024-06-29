from airline import dependencies
from nameko.rpc import rpc

class AirlineService:
    name = 'lion_air_service'

    database = dependencies.Database()

    @rpc
    def get_all_airport(self):
        objects = self.database.get_all_airport()
        return objects
    
    @rpc
    def get_all_flight(self):
        objects = self.database.get_all_flight()
        return objects
    
    @rpc
    def get_flight(self, airport_origin_location_code, airport_destination_location_code, date):
        object = self.database.get_flight(airport_origin_location_code, airport_destination_location_code, date)
        return object

    @rpc
    def post_ticket(self, customer_name, flight_code, date, class_name):
        object = self.database.post_ticket(customer_name, flight_code, date, class_name)
        return object
    
    @rpc
    def get_ticket(self, customer_name):
        object = self.database.get_ticket(customer_name)
        return object
