# db.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="",     # Địa chỉ IP của Raspberry Pi
        user="",           # Tên đăng nhập MySQL
        password="",        # Mật khẩu MySQL
        database=""     # Tên database
    )
