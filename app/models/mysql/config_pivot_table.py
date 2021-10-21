#!/usr/local/bin/python
from typing import Any, AnyStr, Dict
from vendor import Model
from datetime import datetime
from contextlib import closing

"""
Rename the class and the file name if you need generate a pivot table for configs
"""
class ConfigPivotTable(Model):
    _table = 'config_pivot_table'
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
