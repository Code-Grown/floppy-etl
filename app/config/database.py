#!/usr/local/bin/python
from os import environ as env

# Connection driver
DB_CONNECTIONS = {

    'mongodb': {
        'conn_string': env.get('DBM_CONNECTION_STRING'),
        'driver': env.get('DBM_CONNECTION_DRIVER'),
        'url': '',
        'host': env.get('DBM_HOST'),
        'replicaset': env.get('DBM_REPLICASET'),
        'port': env.get('DBM_PORT'),
        'database': env.get('DBM_DB'),
        'username': env.get('DBM_USER'),
        'password': env.get('DBM_PASSWORD'),
        'auth_source': env.get('DBM_AUTH_SOURCE'),
        'auth_mechanism': env.get('DBM_AUTH_MECHANISM'),
        'charset': '',
        'prefix': '',
        'prefix_indexes': ''
    },

    'mysql': {
        'conn_string': env.get('DBMY_CONNECTION_STRING'),
        'driver': env.get('DBMY_CONNECTION_DRIVER'),
        'url': '',
        'host': env.get('DBMY_HOST'),
        'port': env.get('DBMY_PORT'),
        'database': env.get('DBMY_DB'),
        'username': env.get('DBMY_USER'),
        'password': env.get('DBMY_PASSWORD'),
        'unix_socket': '',
        'charset': 'utf8',
        'collation': '',
        'prefix': '',
        'prefix_indexes': '',
        'strict': '',
        'engine': ''
    },

    'pgsql': {
        'driver': env.get('DBPG_CONNECTION_DRIVER'),
        'url': '',
        'host': env.get('DBPG_HOST'),
        'port': env.get('DBPG_PORT'),
        'database': env.get('DBPG_DB'),
        'username': env.get('DBPG_USER'),
        'password': env.get('DBPG_PASSWORD'),
        'charset': '',
        'prefix': '',
        'prefix_indexes': '',
        'schema': '',
        'sslmode': ''
    },

    'sqlsrv': {
        'driver': env.get('DBMS_CONNECTION_DRIVER'),
        'url': '',
        'host': env.get('DBMS_HOST'),
        'port': env.get('DBMS_PORT'),
        'database': env.get('DBMS_DB'),
        'username': env.get('DBMS_USER'),
        'password': env.get('DBMS_PASSWORD'),
        'charset': '',
        'prefix': '',
        'prefix_indexes': ''
    },

    'sqlite': {
        'driver': env.get('DBSQLT_CONNECTION_DRIVER'),
        'url': '',
        'host': env.get('DBSQLT_HOST'),
        'port': env.get('DBSQLT_PORT'),
        'database': env.get('DBSQLT_DB'),
        'username': env.get('DBSQLT_USER'),
        'password': env.get('DBSQLT_PASSWORD'),
        'prefix': '',
    }

}
