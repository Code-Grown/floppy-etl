#!/usr/local/bin/python
from typing import Any
import argparse, importlib
import sys, pdb

from config import ARGUMENT_LIST, CORE_ARGUMENT_LIST, PASSIVE_ARGUMENT_LIST, \
    ARGUMENTS_DIR_MODULE, CORE_ARGUMENTS_DIR_MODULE, PASSIVE_ARGUMENTS_DIR_MODULE, \
    PARSER_ARGUMENT_DESCRIPTION


class Argument:

    def __init__(self):
        pass

    @staticmethod
    def execute_arguments(parser_arguments: Any,
                          argument: Any,
                          argument_value: Any,
                          args_bag: Any,
                          typeargument: Any) -> None:
        try:
            # Location of command name based on created command file
            argument_path = f'.{argument}'

            # Check the directory to get the file associated at argument
            DIR_MODULE = None
            if typeargument == 'core':
                DIR_MODULE = CORE_ARGUMENTS_DIR_MODULE
            elif typeargument == 'passive':
                DIR_MODULE = PASSIVE_ARGUMENTS_DIR_MODULE
            elif typeargument == 'normal':
                DIR_MODULE = ARGUMENTS_DIR_MODULE

            # Loads all arguments of directory
            IMPORTED_ARGUMENT_MODULE = importlib.import_module(
                name=argument_path,
                package=DIR_MODULE
            )

            # Take the created argument in directory and execute it with the default main function
            return IMPORTED_ARGUMENT_MODULE.main(args_bag)

        except:
            e = sys.exc_info()[0]
            print(e)

    def read_arguments(self):
        try:

            # Initialize param parser object
            parser_arguments = argparse.ArgumentParser(description=PARSER_ARGUMENT_DESCRIPTION)


            # Register all core arguments
            # These arguments make it possible to provide the framework with facilities to create functionalities or cover other needs.
            for argument in CORE_ARGUMENT_LIST:

                if 'action' in argument:
                    parser_arguments.add_argument(
                        f"-{argument['argument']}",
                        f"--{argument['fullargument']}",
                        action=argument['action'],
                        help=argument['help'],
                    )
                else:
                    parser_arguments.add_argument(
                        f"-{argument['argument']}",
                        f"--{argument['fullargument']}",
                        metavar=argument['metavar'],
                        help=argument['help'],
                    )


            # Register all passive arguments (additional functions that do not necessarily need accompanying value)
            # These arguments accompany and allow to carry out additional functions or decision-making at particular times
            for argument in PASSIVE_ARGUMENT_LIST:

                if 'action' in argument:
                    parser_arguments.add_argument(
                        f"-{argument['argument']}",
                        f"--{argument['fullargument']}",
                        action=argument['action'],
                        help=argument['help'],
                    )
                else:
                    parser_arguments.add_argument(
                        f"-{argument['argument']}",
                        f"--{argument['fullargument']}",
                        metavar=argument['metavar'],
                        help=argument['help'],
                    )


            # Register all arguments availables and configured on config/argument.py
            # These arguments are the ones that the user defines, and they should not coincide with the existing ones, although it can be configured
            for argument in ARGUMENT_LIST:
                try:
                    if 'action' in argument:
                        parser_arguments.add_argument(
                            f"-{argument['argument']}",
                            f"--{argument['fullargument']}",
                            action=argument['action'],
                            help=argument['help'],
                        )
                    else:
                        parser_arguments.add_argument(
                            f"-{argument['argument']}",
                            f"--{argument['fullargument']}",
                            metavar=argument['metavar'],
                            help=argument['help'],
                        )
                except:
                    print(f"The short argument -> {argument['argument']} (to {argument['fullargument']}) is already registered.")
                    print(f"please use another name to the argument.")
                    print(f"Stop execution.")
                    return


            # Realize parse matching of called arguments
            ARGUMENTS = parser_arguments.parse_args()

            #print(ARGUMENTS)
            #return

            #print(ARGUMENT_LIST + PASSIVE_ARGUMENT_LIST + CORE_ARGUMENT_LIST)
            #return

            AVAILABLE_ARGUMENTS = CORE_ARGUMENT_LIST + PASSIVE_ARGUMENT_LIST + ARGUMENT_LIST

            # args_bag is the list of arguments that have value add additional options or provide parameterization
            args_bag = []
            # exec_args is the list of arguments that do the direct execution
            exec_args = []

            #print(AVAILABLE_ARGUMENTS)
            #return

            # Filter the selected or called arguments to later execute them with it main function
            # Engine that's validate if argument has a value
            #for item in ARGUMENT_LIST:
            for item in AVAILABLE_ARGUMENTS:

                fullargument = item['fullargument']
                result_eval = eval(f"ARGUMENTS.{fullargument}")

                #print(f"{fullargument}: {result_eval}")
                #print(fullargument)
                #continue

                # Check if the command is called or invoked and catch it value
                if (value := eval(f"ARGUMENTS.{fullargument}")) is not False:
                    #print(f"ARGUMENTS.{fullargument}")
                    #print(f"{fullargument}: {value}")
                    #continue



                    # if the argument has a value, append the argument directly with associated value
                    #if value is True:
                    #    if 'strict' in item:
                    #        args_bag.append({fullargument: value})
                    #    else:
                    #        typeargument = 'normal'
                    #        if 'typeargument' in item:
                    #            typeargument = item['typeargument']
                    #        exec_args.append({
                    #            'name': fullargument,
                    #            'value': value,
                    #            'argument': item['argument'],
                    #            'typeargument': typeargument
                    #        })
                    #else:
                    #    if value is not None:
                    #        args_bag.append({fullargument:value})


                    # if the argument has a value and has strict param, the argument is added directly with the associated value in args_bag
                    # This is done this way because the arguments that have value add extra options or provide parameterization to the direct execution arguments.
                    if value is True:

                        if 'strict' in item:
                            args_bag.append({fullargument: value})

                        # Allows to differentiate the arguments configured by the user with those of the core
                        typeargument = 'normal' # <- normal is the default option
                        if 'typeargument' in item:
                            typeargument = item['typeargument']

                        # Here is added to list of arguments of direct execution
                        exec_args.append({
                            'name': fullargument,
                            'value': value,
                            'argument': item['argument'],
                            'typeargument': typeargument
                        })

                    # otherwise, if the value is not None, the argument is added directly with the associated value in args_bag
                    else:
                        if value is not None:
                            args_bag.append({fullargument:value})
                #else:
                    #print(f"ARGUMENTS.{fullargument}")
                    #print(f"{fullargument}: {value}")
                    #continue
                    #pass

            #print(exec_args)
            #print(args_bag)
            #return

            #print(args_bag, exec_args)
            for exec in exec_args:
                argument_value = eval(f"ARGUMENTS.{exec['name']}")
                self.execute_arguments(
                    parser_arguments=parser_arguments,
                    argument=exec['argument'],
                    argument_value=argument_value,
                    args_bag=args_bag,
                    typeargument=exec['typeargument'],
                )
            return
        except:
            import sys
            #print(f'System info: {sys.exc_info()[0]}')
            sys.exit()
            #print("Unknown Error: {}".format(ve))
            #return False
