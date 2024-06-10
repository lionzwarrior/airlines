from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None


    def __init__(self, connection):
        self.connection = connection


    def get_all_airport(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM `airport`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'name': row['name'],
                'location_code': row['location_code'],
                'city_name': row['city_name']
            })
        cursor.close()
        return result


    def get_flight(self, airport_origin_location_code, airport_destination_location_code, date):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT f.* FROM (SELECT fc.flight_code, ao.name AS airport_origin_name, ao.location_code AS airport_origin_location_code, ao.city_name AS airport_origin_city_name, ad.name AS airport_destination_name, ad.location_code AS airport_destination_location_code, ad.city_name AS airport_destination_city_name, fc.start_time, fc.end_time, c.name AS class_name, f.capacity, f.price, f.date, f.weight, f.delay FROM `flight` f INNER JOIN `flight_code` fc ON f.flight_code_id = fc.id INNER JOIN airport ao ON ao.id = fc.airport_origin_id INNER JOIN airport ad ON ad.id = fc.airport_destination_id INNER JOIN `class` c ON c.id = f.class_id) f WHERE f.airport_origin_location_code = '{airport_origin_location_code}' AND f.airport_destination_location_code = '{airport_destination_location_code}' AND date = '{date}';"
        result = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            temp_start_time = row["start_time"].total_seconds()
            hours, remainder = divmod(temp_start_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            temp_finish_time = row["end_time"].total_seconds()
            hours2, remainder2 = divmod(temp_finish_time, 3600)
            minutes2, seconds2 = divmod(remainder2, 60)
            row['start_time'] = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
            row['end_time'] = '{:02}:{:02}:{:02}'.format(int(hours2), int(minutes2), int(seconds2))
            row['date'] = row['date'].strftime('%Y/%m/%d')
            result.append({
                'flight_code': row['flight_code'],
                'airport_origin_name': row['airport_origin_name'],
                'airport_origin_location_code': row['airport_origin_location_code'],
                'airport_origin_city_name': row['airport_origin_city_name'],
                'airport_destination_name': row['airport_destination_name'],
                'airport_destination_location_code': row['airport_destination_location_code'],
                'airport_destination_city_name': row['airport_destination_city_name'],
                'start_time': row['start_time'],
                'end_time': row['end_time'],
                'class_name': row['class_name'],
                'capacity': row['capacity'],
                'price': row['price'],
                'date': row['date'],
                'weight': row['weight'],
                'delay': row['delay']
            })
        cursor.close()
        return result


    def post_ticket(self, flight_id, date, start_time, finish_time):
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
