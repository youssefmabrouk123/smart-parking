from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

mysql = MySQL()

class User:
    @staticmethod
    def get_by_email(email):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cur.fetchone()
        cur.close()
        return user

    @staticmethod
    def create(name, email, password):
        cur = mysql.connection.cursor()
        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", 
                    (name, email, hashed_password))
        mysql.connection.commit()
        cur.close()

class ParkingSpace:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT ps.id, ps.space_number, 
                   CASE WHEN r.id IS NULL THEN 'free' ELSE 'taken' END as status
            FROM parking_spaces ps
            LEFT JOIN reservations r ON ps.id = r.space_id AND 
                                       r.end_time > NOW()
            ORDER BY ps.space_number
        """)
        spaces = cur.fetchall()
        cur.close()
        return spaces

    @staticmethod
    def get_by_id(space_id):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT ps.* FROM parking_spaces ps
            LEFT JOIN reservations r ON ps.id = r.space_id AND 
                                     r.end_time > NOW()
            WHERE ps.id = %s AND r.id IS NULL
        """, [space_id])
        space = cur.fetchone()
        cur.close()
        return space

class Reservation:
    @staticmethod
    def create(user_id, space_id, hours):
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=hours)
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO reservations(user_id, space_id, start_time, end_time) 
            VALUES(%s, %s, %s, %s)
        """, (user_id, space_id, start_time, end_time))
        reservation_id = cur.lastrowid
        mysql.connection.commit()
        cur.close()
        return reservation_id, start_time, end_time

    @staticmethod
    def get_by_user(user_id):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT r.id, r.start_time, r.end_time, ps.space_number
            FROM reservations r
            JOIN parking_spaces ps ON r.space_id = ps.id
            WHERE r.user_id = %s
            ORDER BY r.start_time DESC
        """, [user_id])
        reservations = cur.fetchall()
        cur.close()
        return reservations or []  # Return empty list if no reservations