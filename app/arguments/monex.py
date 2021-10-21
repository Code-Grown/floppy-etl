#!/usr/local/bin/python
from typing import Any
from vendor import Log

"""
    Method Required: This method allows this argument to be executed, it will execute everything included in this block.
"""
def main( args_bag: Any ) -> None:
    monitor_example(args_bag)

def monitor_example(args_bag: Any) -> None:
    log_hint = '[monitor_example]'
    Log.info(f'Example: {log_hint} monitoring service [Example].')
