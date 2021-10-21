
#!/usr/local/bin/python
from typing import Any


"""
    Method Required: This method allows this argument to be executed, it will execute everything included in this block.
"""
def main( args_bag: Any ) -> None:
    show_version()

def show_version() -> None:
    print("""
  █████▒██▓     ▒█████   ██▓███   ██▓███ ▓██   ██▓   ▓█████▄▄▄█████▓ ██▓
▓██   ▒▓██▒    ▒██▒  ██▒▓██░  ██▒▓██░  ██▒▒██  ██▒   ▓█   ▀▓  ██▒ ▓▒▓██▒
▒████ ░▒██░    ▒██░  ██▒▓██░ ██▓▒▓██░ ██▓▒ ▒██ ██░   ▒███  ▒ ▓██░ ▒░▒██░
░▓█▒  ░▒██░    ▒██   ██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒ ░ ▐██▓░   ▒▓█  ▄░ ▓██▓ ░ ▒██░
░▒█░   ░██████▒░ ████▓▒░▒██▒ ░  ░▒██▒ ░  ░ ░ ██▒▓░   ░▒████▒ ▒██▒ ░ ░██████▒
 ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒░ ░ ▒ ░░   ░ ▒░▓  ░
 ░     ░ ░ ▒  ░  ░ ▒ ▒░ ░▒ ░     ░▒ ░     ▓██ ░▒░     ░ ░  ░   ░    ░ ░ ▒  ░
 ░ ░     ░ ░   ░ ░ ░ ▒  ░░       ░░       ▒ ▒ ░░        ░    ░        ░ ░
           ░  ░    ░ ░                    ░ ░           ░  ░            ░  ░
                                          ░ ░
    """)
    print("Version 1.0.0")
