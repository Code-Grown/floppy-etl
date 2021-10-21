
#!/usr/local/bin/python
from typing import Any


"""
    Method Required: This method allows this argument to be executed, it will execute everything included in this block.
"""
def main( args_bag: Any ) -> None:
    make_argument(args_bag)

def make_argument(args_bag) -> None:

    print(args_bag)
    print("Making an argument! :D yay!")
