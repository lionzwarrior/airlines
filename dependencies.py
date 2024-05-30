from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def add_reservation(self, customer_name, ticket_id, chair_number_id, gateway_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT f.capacity - (SELECT COUNT(*) FROM reservation r WHERE r.ticket_id = t.id) AS count FROM `ticket` t INNER JOIN flight f ON t.flight_id = f.id WHERE t.id = {ticket_id} GROUP BY t.id"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result['count'] > 0:
                sql = f"INSERT INTO `reservation`(`customer_name`, `ticket_id`, `chair_number_id`, `gateway_id`) VALUES ('{customer_name}', '{ticket_id}','{chair_number_id}','{gateway_id}')"
                cursor.execute(sql)
                self.connection.commit()
                response = {
                    "status": "success",
                    "message": "Reservation added successfully",
                    "data": {
                        "ticket_id": ticket_id,
                        "chair_number_id": chair_number_id,
                        "gateway_id": gateway_id
                    }
                }
            elif result['count'] <= 0:
                response = {
                    "status": "unavailable",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Reservation with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response


    def get_all_reservations(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        # sql = "SELECT r.id, c.name AS class, ao.name AS airport_origin, ad.name AS airport_destination, f.weight_limit, t.start_datetime, t.end_datetime, r.timestamp FROM `reservation` r INNER JOIN ticket t ON r.ticket_id = t.id INNER JOIN flight f ON t.flight_id = f.id INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id"
        sql = f"SELECT * FROM `reservation`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'customer_name': row["customer_name"],
                'ticket_id': row['ticket_id'],
                'chair_number_id': row['chair_number_id'],
                'gateway_id': row['gateway_id'],
                # 'class': row['class'],
                # 'airport_origin': row['airport_origin'],
                # 'airport_destination': row['airport_destination'],
                # 'weight_limit': row['weight_limit'],
                # 'start_datetime': row['start_datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                # 'end_datetime': row['end_datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                'timestamp': row['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
            })
        cursor.close()
        return result
    
    def get_reservation(self, id):
        cursor = self.connection.cursor(dictionary=True)
        # sql = f"SELECT r.id, c.name AS class, ao.name AS airport_origin, ad.name AS airport_destination, f.weight_limit, t.start_datetime, t.end_datetime, r.timestamp FROM `reservation` r INNER JOIN ticket t ON r.ticket_id = t.id INNER JOIN flight f ON t.flight_id = f.id INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id WHERE r.id = {id}"
        sql = f"SELECT * FROM `reservation` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            result['timestamp'] = result['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            # result['start_datetime'] = result['start_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            # result['end_datetime'] = result['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"reservation with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_reservation(self, id, customer_name, ticket_id, chair_number_id, gateway_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `reservation` SET `customer_name`='{customer_name}', `ticket_id`='{ticket_id}',`chair_number_id`='{chair_number_id}',`gateway_id`='{gateway_id}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"reservation with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"reservation with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_reservation(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM reservation WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"reservation with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"reservation with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def add_ticket(self, flight_id, date, start_time, finish_time):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `ticket`(`flight_id`, `date`, `start_time`, `finish_time`) VALUES ('{flight_id}','{date}','{start_time}','{finish_time}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Ticket added successfully",
                "data": {
                    "flight_id": flight_id,
                    "date": date,
                    "start_time": start_time,
                    "finish_time": finish_time
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response


    def get_all_tickets(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        # sql = "SELECT t.id, c.name AS class, ao.name AS airport_origin, ad.name AS airport_destination, f.weight_limit, f.price, t.start_datetime, t.end_datetime FROM `ticket` AS t INNER JOIN flight f ON t.flight_id = f.id INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id"
        sql = f"SELECT * FROM `ticket`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            temp_start_time = row["start_time"].total_seconds()
            hours, remainder = divmod(temp_start_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            temp_finish_time = row["finish_time"].total_seconds()
            hours2, remainder2 = divmod(temp_finish_time, 3600)
            minutes2, seconds2 = divmod(remainder2, 60)
            result.append({
                'id': row['id'],
                'flight_id': row['flight_id'],
                'date': row['date'].strftime('%Y/%m/%d'),
                'start_time': '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)),
                'finish_time': '{:02}:{:02}:{:02}'.format(int(hours2), int(minutes2), int(seconds2)),
                # 'class': row['class'],
                # 'airport_orign': row['airport_origin'],
                # 'airport_destination': row['airport_destination'],
                # 'weight_limit': row['weight_limit'],
                # 'price': row['price'],
                # 'start_datetime': row['start_datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                # 'end_datetime': row['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            })
        cursor.close() 
        return result
    
    def get_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        # sql = f"SELECT t.id, c.name AS class, ao.name AS airport_origin, ad.name AS airport_destination, f.weight_limit, f.price, t.start_datetime, t.end_datetime FROM `ticket` AS t INNER JOIN flight f ON t.flight_id = f.id INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id WHERE t.id = {id}"
        sql = f"SELECT * FROM `ticket` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            temp_start_time = result["start_time"].total_seconds()
            hours, remainder = divmod(temp_start_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            temp_finish_time = result["finish_time"].total_seconds()
            hours2, remainder2 = divmod(temp_finish_time, 3600)
            minutes2, seconds2 = divmod(remainder2, 60)
            result['start_time'] = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
            result['finish_time'] = '{:02}:{:02}:{:02}'.format(int(hours2), int(minutes2), int(seconds2))
            result['date'] = result['date'].strftime('%Y/%m/%d')
            # result['start_datetime'] = result['start_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            # result['end_datetime'] = result['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"ticket with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_ticket(self, id, flight_id, date, start_time, finish_time):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `ticket` SET `flight_id`='{flight_id}',`date`='{date}',`start_time`='{start_time}',`finish_time`='{finish_time}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Ticket with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Ticket with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `ticket` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Ticket with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Ticket with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def add_flight(self, airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `flight`(`airline_id`, `class_id`, `airport_origin_id`, `airport_destination_id`, `capacity`, `weight_limit`, `price`) VALUES ('{airline_id}','{class_id}','{airport_origin_id}','{airport_destination_id}','{capacity}','{weight_limit}','{price}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Flight added successfully",
                "data": {
                    "airline_id": airline_id,
                    "class_id": class_id,
                    "airport_origin": airport_origin_id,
                    "airport_destination": airport_destination_id,
                    "capacity": capacity,
                    "weight_limit": weight_limit,
                    "price": price
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response


    def get_all_flights(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        # sql = "SELECT f.id, c.name AS class, ao.name AS airport_origin, ad.name AS airport_destination, f.capacity, f.weight_limit, f.price FROM `flight` f INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id"
        sql = f"SELECT * FROM `flight`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'airline_id': row['airline_id'],
                'class_id': row['class_id'],
                'airport_origin_id': row['airport_origin_id'],
                'airport_destination_id': row['airport_destination_id'],
                # 'class': row['class'],
                # 'airport_origin': row['airport_origin'],
                # 'airport_destination': row['airport_destination'],
                'capacity': row['capacity'],
                'weight_limit': row['weight_limit'],
                'price': row['price']
            })
        cursor.close()
        return result
    
    def get_flight(self, id):
        cursor = self.connection.cursor(dictionary=True)
        # sql = f"SELECT f.id, c.name, ao.name AS airport_origin, ad.name AS airport_destination, f.capacity, f.weight_limit, f.price FROM `flight` f INNER JOIN class c ON f.class_type = c.id INNER JOIN airport ao ON f.airport_origin = ao.id INNER JOIN airport ad ON f.airport_destination = ad.id WHERE f.id = {id}"
        sql = f"SELECT * FROM `flight` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Flight with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_flight(self, id, airline_id, class_id, airport_origin_id, airport_destination_id, capacity, weight_limit, price):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `flight` SET `airline_id`='{airline_id}',`class_id`='{class_id}',`airport_origin_id`='{airport_destination_id}',`airport_destination_id`='{airport_destination_id}',`capacity`='{capacity}',`weight_limit`='{weight_limit}',`price`='{price}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Flight with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Flight with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def delete_flight(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `flight` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Flight with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Flight with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def add_class(self, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `class`(`name`) VALUES ('{name}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Class added successfully",
                "data": {
                    "name": name
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def get_all_class(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `class`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name']
            })
        cursor.close()
        return result
    
    def get_class(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM `class` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Class with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_class(self, id, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `class` SET `name`='{name}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Class with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Class with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_class(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `class` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Class with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Class with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def add_airport(self, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `airport`(`name`) VALUES ('{name}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Airport added successfully",
                "data": {
                    "name": name
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def get_all_airport(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `airport`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name']
            })
        cursor.close()
        return result
    
    def get_airport(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM `airport` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Airport with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_airport(self, id, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `airport` SET `name`='{name}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Airport with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Airport with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_airport(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `airport` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Airport with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Airport with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def add_airline(self, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `airline`(`name`) VALUES ('{name}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Airline added successfully",
                "data": {
                    "name": name
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def get_all_airline(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `airline`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name']
            })
        cursor.close()
        return result
    
    def get_airline(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM `airline` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Airline with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_airline(self, id, name):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `airline` SET `name`='{name}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Airline with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Airline with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_airline(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `airline` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Airline with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Airline with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def add_chair_number(self, name, flight_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `chair_number`(`name`, `flight_id`) VALUES ('{name}', '{flight_id}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Chair Number added successfully",
                "data": {
                    "name": name,
                    "flight_id": flight_id
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def get_all_chair_number(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `chair_number`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'flight_id': row['flight_id']
            })
        cursor.close()
        return result
    
    def get_chair_number(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM `chair_number` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Chair Number with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_chair_number(self, id, name, flight_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `chair_number` SET `name`='{name}', `flight_id`='{flight_id}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Chair Number with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Chair Number with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_chair_number(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `chair_number` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Chair Number with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Chair Number with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response
    
    def add_gateway(self, name, airport_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `gateway`(`name`, `airport_id`) VALUES ('{name}', '{airport_id}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Gateway added successfully",
                "data": {
                    "name": name,
                    "airport_id": airport_id
                }
            }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def get_all_gateway(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `gateway`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'airport_id': row['airport_id']
            })
        cursor.close()
        return result
    
    def get_gateway(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM `gateway` WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                response = {
                    "status": "success",
                    "data": result
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Chair Number with id {id} not found"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def edit_gateway(self, id, name, airport_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"UPDATE `gateway` SET `name`='{name}', `airport_id`='{airport_id}' WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_updated = cursor.rowcount
            if rows_updated == 0:
                response = {
                    "status": "not_found",
                    "message": f"Gateway with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Gateway with id {id} edited successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def delete_gateway(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"DELETE FROM `gateway` WHERE id = {id}"
        try:
            cursor.execute(sql)
            self.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted == 0:
                response = {
                    "status": "not_found",
                    "message": f"Gateway with id {id} not found"
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Gateway with id {id} deleted successfully"
                }
        except Exception as e:
            response = {
                "status": str(e)
            }
        finally:
            cursor.close()
        return response

    def __del__(self):
        self.connection.close()


class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='127.0.0.1',
                database='airline',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
