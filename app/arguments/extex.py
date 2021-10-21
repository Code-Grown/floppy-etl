#!/usr/local/bin/python
from typing import Any
from vendor import Log
from datetime import timedelta, datetime

"""
    Method Required: This method allows this argument to be executed, it will execute everything included in this block.
"""
def main( args_bag: Any ) -> None:
    extract_example(args_bag)

def extract_example(args_bag: Any) -> None:
    date_yesterday = datetime.strftime(datetime.now() - timedelta(days=1), '%Y-%m-%d')
    log_hint = '[extract_example]'
    Log.info(f'Example: {log_hint} extracting data from yesterday -> : {date_yesterday}.')
