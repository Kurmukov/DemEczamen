from peewee import *
from SRC.Connection.conect import connect, mysql_db


class Base(Model):
    class Meta:
        database = mysql_db