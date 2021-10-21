#!/usr/local/bin/python
from vendor import Argument, Log
from config import DEBUG
import sys, pdb


class Application(Argument):

    def __init__(self):
        pass

    def init_application(self):
        try:
            Log.info('Init Application, reading arguments.')
            self.read_arguments()
        except:
            Log.danger('Application Stopped')
            Log.critical(sys.exc_info()[0])
        finally:
            if DEBUG:
                Log.info(f"Application Ended.")
                Log.info(f'System info: {sys.exc_info()[0]}')
                sys.exit()


if __name__ == '__main__':
    Application().init_application()
