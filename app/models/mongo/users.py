#!/usr/local/bin/python
from typing import Any, AnyStr, Dict
from vendor import Model, Log
from datetime import datetime as dt, timedelta as td


class User(Model):
    _table = 'users'
    _primary_key = 'id'
    _driver = 'mongodb'
    _connection = None
    _db = None

    def __init__(self):
        super().__init__(
            self._table,
            self._primary_key,
            self._driver
        )
        self._connection = self.connect_database()
