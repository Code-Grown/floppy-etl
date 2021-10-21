#!/usr/local/bin/python
from typing import Any, AnyStr
from pymongo import MongoClient
import pymysql
from config import DB_CONNECTIONS
from contextlib import closing
from vendor import Log

class Model:

    _table = str
    _primary_key = str
    _driver = str
    _db = None
    _connection = None
    _client = None

    def __init__(self, table, primary_key, driver = None):
        self._table = table
        self._primary_key = primary_key
        self._driver = driver

    def connect_database(self):
        self._connection = None

        config = DB_CONNECTIONS[self._driver]

        if self._driver == 'mongodb':
            try:
                if config['conn_string'] is not None:
                    self._client = MongoClient(config["conn_string"])
                    self._connection = getattr(self._client, config['database'])
                else:
                    self._client = MongoClient(
                        f'{config["host"]}:{config["port"]}',
                        username=f'{config["username"]}',
                        password=f'{config["password"]}',
                        authSource=f'{config["auth_source"]}',
                        authMechanism=f'{config["auth_mechanism"]}',
                        #replicaset=f'{config["replicaset"]}'
                    )
                    self._connection = self._client[config['database']]
            except:
                Log.danger(f'Error al conectar a la base MongoDB')

        elif self._driver == 'mysql':
            try:
                self._connection = pymysql.connect(
                    host=f'{config["host"]}',
                    user=f'{config["username"]}',
                    password=f'{config["password"]}',
                    database=f'{config["database"]}',
                    charset=f'{config["charset"]}',
                    port=int(f'{config["port"]}')
                )
                self.disable_autocommit()
            except:
                Log.danger(f'Error al conectar a la base Mysql')

        return self._connection

    def disconnect_database(self):
        if self._driver == 'mongodb':
            self._client.close()
        elif self._driver == 'mysql':
            self._connection.close()

    """
    Only Mysql
    """
    def enable_autocommit(self):
        with closing( self._connection.cursor() ) as cursor:
            cursor = self._connection.cursor()
            cursor.execute('SET autocommit = 1')
            self._connection.commit()

    """
    Only Mysql
    """
    def disable_autocommit(self):
        with closing( self._connection.cursor() ) as cursor:
            cursor = self._connection.cursor()
            cursor.execute('SET autocommit = 0')
            self._connection.commit()

    """
    Only Mysql
    """
    def commit_transactions(self):
        self._connection.commit()

    """
    Only Mysql
    """
    def truncate_table(self):
        with closing( self._connection.cursor() ) as cursor:
            cursor = self._connection.cursor()
            cursor.execute(f"TRUNCATE TABLE { self._table };")
            self._connection.commit()

    """
    Only Mysql
    """
    def get_last_day_of_current_month(self) -> Any:
        with closing(self._connection.cursor()) as cursor:
            query = f"SELECT LAST_DAY(NOW())"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]

    """
    Only Mysql
    """
    def get_last_day_of_month_from_date(self, past_day: AnyStr) -> Any:
        with closing(self._connection.cursor()) as cursor:
            query = f"SELECT LAST_DAY('{past_day}')"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]

    """
    Only Mysql
    """
    def get_first_day_of_current_month(self) -> Any:
        with closing(self._connection.cursor()) as cursor:
            query = f"SELECT LAST_DAY(NOW() - INTERVAL 1 MONTH) + INTERVAL 1 DAY"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]

    """
    Only Mysql
    """
    def get_first_day_of_past_month(self) -> Any:
        with closing(self._connection.cursor()) as cursor:
            query = f"SELECT LAST_DAY(NOW() - INTERVAL 2 MONTH) + INTERVAL 1 DAY"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]

    """
    Only Mysql
    """
    def get_first_day_of_months_back(self, interval: Any=1) -> Any:
        with closing(self._connection.cursor()) as cursor:
            query = f"SELECT LAST_DAY(NOW() - INTERVAL {interval} MONTH) + INTERVAL 1 DAY"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]
