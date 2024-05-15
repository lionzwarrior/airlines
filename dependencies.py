from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def add_ticket(self, ticket_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `ticket`(`ticket_id`) VALUES ({ticket_id})"
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


    def get_all_tickets(self):
        cursor = self.connection.cursor(dictionary=True)
        reservation = []
        sql = "SELECT * FROM ticket"
        cursor.execute(sql)
        for row in cursor.fetchall():
            reservation.append({
                'id': row['id'],
                'ticket_id': row['ticket_id'],
                'timestamp': row['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
            })
        cursor.close()
        return reservation
    
    def get_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM ticket WHERE id = {id}"
        try:
            cursor.execute(sql)
            reservation = cursor.fetchone()
            reservation['timestamp'] = reservation['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            if reservation:
                response = {
                    "status": "success",
                    "data": reservation
                }
            else:
                response = {
                    "status": "not_found",
                    "message": f"Ticket with id {id} not found"
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
        sql = f"DELETE FROM ticket WHERE id = {id}"
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

    def add_ticket(self, ticket_type, start_datetime, end_datetime):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `ticket`(`ticket_type`, `start_datetime`, `end_datetime`) VALUES ('{ticket_type}','{start_datetime}','{end_datetime}')"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Room added successfully",
                "data": {
                    "ticket_type": ticket_type,
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
        reservation = []
        sql = "SELECT * FROM ticket"
        cursor.execute(sql)
        for row in cursor.fetchall():
            reservation.append({
                'id': row['id'],
                'ticket_type': row['ticket_type'],
                'start_datetime': row['start_datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                'end_datetime': row['end_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            })
        cursor.close()
        return reservation
    
    def get_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM ticket WHERE id = {id}"
        try:
            cursor.execute(sql)
            reservation = cursor.fetchone()
            reservation['timestamp'] = reservation['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            if reservation:
                response = {
                    "status": "success",
                    "data": reservation
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
