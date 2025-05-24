# db.py

import mysql.connector

# def get_db_connection():
#     return mysql.connector.connect(
#         host="",     # Địa chỉ IP của Raspberry Pi
#         user="",           # Tên đăng nhập MySQL
#         password="",        # Mật khẩu MySQL
#         database=""     # Tên database
#     )
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('light.db')  # file SQLite bạn đang dùng
    return conn
