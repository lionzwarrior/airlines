from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def add_reservation(self, ticket_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `reservation`(`ticket_id`) VALUES ({ticket_id})"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Room added successfully",
                "data": {
                    "ticket_id": ticket_id,
                }
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
        sql = "SELECT * FROM reservation"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'ticket_id': row['ticket_id'],
                'timestamp': row['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
            })
        cursor.close()
        return result
    
    def get_reservation(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM reservation WHERE id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            result['timestamp'] = result['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
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

    def add_ticket(self, flight_type, start_datetime, end_datetime):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `ticket`(`flight_type`, `start_datetime`, `end_datetime`) VALUES ('{flight_type}','{start_datetime}','{end_datetime}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Room added successfully",
                "data": {
                    "flight_type": flight_type,
                    "start_datetime": start_datetime,
                    "end_datetime": end_datetime
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
        sql = "SELECT t.id, f.airport_origin, f.airport_destination, f.price, t.start_datetime, t.end_datetime FROM `ticket` as t inner join flight f on t.flight_type = f.id"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'airport_orign': row['airport_origin'],
                'airport_destination': row['airport_destination'],
                'price': row['price'],
                'start_datetime': row['start_datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                'end_datetime': row['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            })
        cursor.close()
        return result
    
    def get_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT t.id, f.airport_origin, f.airport_destination, f.price, t.start_datetime, t.end_datetime FROM `ticket` as t inner join flight f on t.flight_type = f.id WHERE t.id = {id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            result['start_datetime'] = result['start_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            result['end_datetime'] = result['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
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

    def add_flight(self, airport_origin, airport_destination, capacity, price):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `flight`('airport_origin', `airport_destination`, `capacity`, `price`) VALUES ('{airport_origin}', '{airport_destination}','{capacity}','{price}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Room added successfully",
                "data": {
                    "airport_origin": airport_origin,
                    "airport_destination": airport_destination,
                    "capacity": capacity,
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
        sql = "SELECT * FROM `flight`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'airport_origin': row['airport_origin'],
                'airport_destination': row['airport_destination'],
                'capacity': row['capacity'],
                'price': row['price']
            })
        cursor.close()
        return result
    
    def get_flight(self, id):
        cursor = self.connection.cursor(dictionary=True)
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
                    "message": f"ticket with id {id} not found"
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
