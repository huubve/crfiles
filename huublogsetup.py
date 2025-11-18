import sys
import logging
# how to use this module:
# import huublogsetup
# debuglog, infolog, warnlog, errorlog = getCliLoggers(programName:str)

def log_level_maxer(level):
    def maxer(record):
        if record.levelno > level:
            return False
        else:
            return True
    return maxer

class CliLogger(object):
    def __init__(self, programName):

        self.short_formatter = logging.Formatter("{name}:{levelname}: {message}", style="{")
        self.long_formatter = logging.Formatter("{name}\t{levelname}\t{asctime}\t{process}\t{threadName}\t{pathname}\t{module}\t{lineno}\t{message}", style="{")
        self.formatter = self.short_formatter

        self.handler = logging.StreamHandler(sys.stderr)
        self.handler.setLevel("ERROR")
        self.handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(programName)
        self.logger.setLevel("DEBUG")
        self.logger.addHandler(self.handler)

        self.debug = self.logger.debug
        self.info  = self.logger.info
        self.print = self.logger.info
        self.warn  = self.logger.warning
        self.error = self.logger.error
    def set_formatter(self, f):
        self.formatter = f
        self.handler.setFormatter(self.formatter)
 
