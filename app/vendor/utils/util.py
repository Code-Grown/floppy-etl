#!/usr/local/bin/python
from typing import Any
import os
from os import system
from vendor import Log

class Util:

    log = None

    def __init__(self):
        pass

    @staticmethod
    def get_arg_parameter(param: Any, args_bag: Any) -> Any:
        try:
            # return [arg[param] for arg in args_bag if arg[param]][0] if param in args_bag else None
            # return [arg[param] for arg in args_bag if arg[param]][0]
            for arg in args_bag:
                try:
                    if arg[param] is not None:
                        return arg[param]
                except:
                    continue
        except Exception as ex:
            print(f"{ex} arg param doesn't exists, {args_bag}")
            return None

    @staticmethod
    def validate_date_microtime(dt: Any) -> Any:
        if dt is None:
            return None
        else:
            datesplitted = dt.split(" ")
            newdate = datesplitted[0]
            if datesplitted[1].find(".") > -1:
                timesplitted = datesplitted[1].split(".")
                time, microtime = timesplitted[0], timesplitted[1]
            else:
                time, microtime = datesplitted[1], '000000'
            return f'{ newdate } { time }.{ microtime }'
