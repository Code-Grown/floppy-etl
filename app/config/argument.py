#!/usr/local/bin/python
from os import environ as env
from vendor.argument import CORE_ARGUMENTS, PASSIVE_ARGUMENTS

"""
Setup for argument directories and command description
"""
ARGUMENTS_DIR_MODULE = env.get('ARGUMENTS_DIR_MODULE') or "arguments"
CORE_ARGUMENTS_DIR_MODULE = env.get('CORE_ARGUMENTS_DIR_MODULE') or "vendor.argument.core"
PASSIVE_ARGUMENTS_DIR_MODULE = env.get('PASSIVE_ARGUMENTS_DIR_MODULE') or "vendor.argument.passive"
PARSER_ARGUMENT_DESCRIPTION = env.get('PARSER_ARGUMENT_DESCRIPTION') or "Floppy ETL"

"""
Invoked arguments of core app
"""
CORE_ARGUMENT_LIST = CORE_ARGUMENTS
PASSIVE_ARGUMENT_LIST = PASSIVE_ARGUMENTS

"""
argument: is the real name of script file from /app/arguments folder
fullargument: is the complete name to match with parser argument list
the name cannot match with the core arguments
"""
ARGUMENT_LIST = [

    ########################################
    # Extract
    ########################################
    {
        "argument": "extex",
        "fullargument": "extractExample",
        "help": "Example of command that extracts data.",
        "action": "store_true",  # Doesn't requires values for this argument
    },

    ########################################
    # Transform
    ########################################
    {
        "argument": "traex",
        "fullargument": "transformExample",
        "help": "Example of command that transform data.",
        "action": "store_true",  # Doesn't requires values for this argument
    },

    ########################################
    # Load
    ########################################
    {
        "argument": "loaex",
        "fullargument": "loadExample",
        "help": "Example of command that load data.",
        "action": "store_true",  # Doesn't requires values for this argument
    },

    ########################################
    # Reporting
    ########################################
    {
        "argument": "repex",
        "fullargument": "reportExample",
        "help": "Example of command that do a report.",
        "action": "store_true",  # Doesn't requires values for this argument
    },

    ########################################
    # Monitoring
    ########################################
    {
        "argument": "monex",
        "fullargument": "monitorExample",
        "help": "Example of command that do a monitoring.",
        "action": "store_true", # Doesn't requires values for this argument
    },

]
