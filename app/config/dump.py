#!/usr/local/bin/python
from os import environ as env

DUMP_PARENT_PATH = env.get('DUMP_PARENT_PATH') or '/app/storage/dumped'