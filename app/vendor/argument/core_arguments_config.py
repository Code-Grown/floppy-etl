#!/usr/local/bin/python


CORE_ARGUMENTS = [

    ########################################
    # Monitoring
    ########################################
    {
        "argument": "hc",
        "fullargument": "healthCheck",
        "help": "Check the app status.",
        "action": "store_true", # Doesn't requires values for this argument
        "typeargument": "normal",
    },

    ########################################
    # Makers
    ########################################
    {
        "argument": "ma",
        "fullargument": "makeArgument",
        "help": "Create new argument.",
        "action": "store_true", # Doesn't requires values for this argument
        "typeargument": "core",
    },

]
