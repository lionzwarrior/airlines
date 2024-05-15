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
        
    # @rpc
    # def add_flight(self, airport_destination, seats_available, start_timestamp, finish_timestamp)

    @rpc
    def get_all_room_type(self):
        room_types = self.database.get_all_room_type()
        return room_types

    @rpc
    def get_all_room(self):
        rooms = self.database.get_all_room()
        return rooms

    @rpc
    def get_room_by_num(self, num):
        room = self.database.get_room_by_num(num)
        return room

# Method to add a room
# add_room(self, room_num, room_type)
    @rpc
    def add_room(self, room_num, room_type):
        room = self.database.add_room(room_num, room_type)
        return room

# Method to change a room's status (0 to 1, or vice versa)
    @rpc
    def change_room_status(self, room_num):
        room = self.database.change_room_status(room_num)
        return room

# Method to delete a room
    @rpc
    def delete_room(self, room_num):
        room = self.database.delete_room(room_num)
        return room

# Notes: you may replace room_num with id
