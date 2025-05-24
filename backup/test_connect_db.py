# import mariadb

# try:
#     conn = mariadb.connect(
#         user="admin",
#         password="admin",
#         host="192.168.3.109",  # or IP
#         port=3306,
#         database="lamp_db"
#     )
#     print("✅ Connection to MariaDB successful!")
#     conn.close()
# except mariadb.Error as e:
#     print(f"❌ Error connecting to MariaDB: {e}")
