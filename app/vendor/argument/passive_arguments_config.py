#!/usr/local/bin/python


PASSIVE_ARGUMENTS = [

    ########################################
    # Passive / Globals / Usefuls / Utils
    ########################################

    # Info
    {
        "argument": "V",
        "fullargument": "version",
        "help": "Show version of software.",
        "action": "store_true",  # Doesn't requires values for this argument
        "typeargument": "passive", # <- Has associated file
    },
    {
        "argument": "v",
        "fullargument": "verbose",
        "help": "Show verbose text in output.",
        "action": "store_true",  # Doesn't requires values for this argument
        "strict": True,
    },
    {
        "argument": "vl",
        "fullargument": "verbosityLevel",
        "help": "Argument to select and show verbosity with level.",
        "metavar": "1,2,3",
        "choices": "[0, 1, 2]",
        "type": int
    },
    {
        "argument": "ll",
        "fullargument": "logLevel",
        "help": "Argument to set logs with level.",
        "metavar": "1,2,3"
    },

    # Actions
    {
        "argument": "f",
        "fullargument": "force",
        "help": "Argument to force some.",
        "action": "store_true",  # Doesn't requires values for this argument
        "strict": True,
    },
    {
        "argument": "tp",
        "fullargument": "type",
        "help": "Argument type of argument.",
        "metavar": "extract, load or transform"
    },

    # Working with dates
    {
        "argument": "y",
        "fullargument": "year",
        "help": "Provides year argument value.",
        "metavar": "'20XX'"
    },
    {
        "argument": "m",
        "fullargument": "month",
        "help": "Provides month argument value.",
        "metavar": "'01'"
    },
    {
        "argument": "d",
        "fullargument": "day",
        "help": "Provides day argument value.",
        "metavar": "'01'"
    },
    {
        "argument": "from",
        "fullargument": "fromDate",
        "help": "Argument to indicates the begin date.",
        "metavar": "20XX-01-01 (Y-m-d)"
    },
    {
        "argument": "to",
        "fullargument": "toDate",
        "help": "Argument to indicates the end date.",
        "metavar": "20XX-01-31 (Y-m-d)"
    },
    {
        "argument": "dt",
        "fullargument": "date",
        "help": "Argument to indicates the date of some.",
        "metavar": "20XX-01-01 (Y-m-d)"
    },
    {
        "argument": "btw",
        "fullargument": "between",
        "help": "Argument to compare something.",
        "metavar": "Ej: 'a', '0', '20XX-01-01'"
    },
    {
        "argument": "b",
        "fullargument": "by",
        "help": "Argument to append in comparisson.",
        "metavar": "Ej: 'z', '9', '20XX-01-31'"
    },
    {
        "argument": "t",
        "fullargument": "to",
        "help": "Argument to append in comparisson.",
        "metavar": "Ej: 'z', '9', '20XX-01-31'"
    },
    {
        "argument": "a",
        "fullargument": "at",
        "help": "Argument to append in comparisson.",
        "metavar": "Ej: 'z', '9', '20XX-01-31'"
    },
    {
        "argument": "ac",
        "fullargument": "autoCommit",
        "help": "Argument to set autocommit in queries (true or false).",
        "metavar": "True|False",
    },

]
