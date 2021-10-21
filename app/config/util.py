#!/usr/local/bin/python

from os import environ as env
import datetime

DATERANGE_ES = [{
    1 : { 'days': 31, 'month': 'Enero' },
    2 : { 'days': 28, 'month': 'Febrero' },
    3 : { 'days': 31, 'month': 'Marzo' },
    4 : { 'days': 30, 'month': 'Abril' },
    5 : { 'days': 31, 'month': 'Mayo' },
    6 : { 'days': 30, 'month': 'Junio' },
    7 : { 'days': 31, 'month': 'Julio' },
    8 : { 'days': 31, 'month': 'Agosto' },
    9 : { 'days': 30, 'month': 'Septiembre' },
    10 : { 'days': 31, 'month': 'Octubre' },
    11 : { 'days': 30, 'month': 'Noviembre' },
    12 : { 'days': 31, 'month': 'Diciembre' }
}]

DATERANGE_EN = [{
    1 : { 'days': 31, 'month': 'January' },
    2 : { 'days': 28, 'month': 'February' },
    3 : { 'days': 31, 'month': 'March' },
    4 : { 'days': 30, 'month': 'April' },
    5 : { 'days': 31, 'month': 'May' },
    6 : { 'days': 30, 'month': 'June' },
    7 : { 'days': 31, 'month': 'July' },
    8 : { 'days': 31, 'month': 'August' },
    9 : { 'days': 30, 'month': 'September' },
    10 : { 'days': 31, 'month': 'October' },
    11 : { 'days': 30, 'month': 'November' },
    12 : { 'days': 31, 'month': 'December' }
}]

CURRENT_YEAR = datetime.datetime.today().year
