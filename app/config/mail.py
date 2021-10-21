#!/usr/local/bin/python
from os import environ as env

"""
Token if needed
"""
TOKEN_X_API_EX1 = env.get('TOKEN_X_API_EX1') or 'TOKEN_X_API_EX1'

"""
Email(s) to report
"""
EMAIL_REPORT_TO = env.get('EMAIL_REPORT_TO') or 'name@email.example'
