from peewee import *
def db_connect():
    return MySQLDatabase(
        "KurA1234_Fitnes1",
        host = '10.11.13.118',
        user = "KurA1234_adSmart",
        password = "123456",
        port = 3306

    )


if __name__ == "__main__":
    db_connect().connect()