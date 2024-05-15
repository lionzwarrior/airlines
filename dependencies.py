from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def add_ticket(self, flight_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"INSERT INTO `ticket`(`flight_id`) VALUES ({flight_id})"
        try:
            cursor.execute(sql)
            self.connection.commit()
            response = {
                "status": "success",
                "message": "Room added successfully",
                "data": {
                    "flight_id": flight_id,
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
        sql = "SELECT * FROM ticket"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'flight_id': row['flight_id'],
                'timestamp': row['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
            })
        cursor.close()
        return result
    
    def get_ticket(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM ticket WHERE id = {id}"
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
