#!/usr/local/bin/python
from vendor import Model


class User(Model):
    _table = 'users'
    _primary_key = 'id'
    _driver = 'mysql'
    _connection = None
    _db = None

    def __init__(self):
        super().__init__(
            self._table,
            self._primary_key,
            self._driver
        )
        self._connection = self.connect_database()
