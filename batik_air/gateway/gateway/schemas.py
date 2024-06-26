from marshmallow import Schema, fields

class ClassSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    

class AirportSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    location_code = fields.Str(required=True)
    city_name = fields.Str(required=True)
    

class FlightCodeSchema(Schema):
    id = fields.Int(required=True)
    flight_code = fields.Str(required=True)
    airport_origin_id = fields.Int(required=True)
    airport_destination_id = fields.Int(required=True)
    start_time = fields.Time(required=True)
    end_time = fields.Time(required=True)
    status = fields.Int(required=True)
    

class FlightSchema(Schema):
    id = fields.Int(required=True)
    flight_code_id = fields.Int(required=True)
    class_id = fields.Int(required=True)
    airport_id = fields.Int(required=True)
    capacity = fields.Int(required=True)
    price = fields.Int(required=True)
    date = fields.Date(required=True)
    weight = fields.Int(required=True)
    delay = fields.Int(required=True)
    status = fields.Int(required=True)
    

class TicketSchema(Schema):
    id = fields.Int(required=True)
    customer_name = fields.Str(required=True)
    flight_id = fields.Int(required=True)
    status = fields.Int(required=True)
    timestamp = fields.Timestamp(required=True)
