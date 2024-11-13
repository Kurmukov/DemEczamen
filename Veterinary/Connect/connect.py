from peewee import*

mysql_db = MySQLDatabase(
'KurA1234_Hostel_DE',
    user = 'KurA1234_Ku_AL12',
    password = '123456',
    host = '10.11.13.118',
    port = 3306
)
if __name__ == "__main__":
    mysql_db.connect()