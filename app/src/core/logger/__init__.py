import logging
from datetime import date
from pathlib import Path

_dark_grey = "\x1b[32;20m"
_grey = "\x1b[38;20m"
_yellow = "\x1b[33;20m"
_red = "\x1b[31;20m"
_bold_red = "\x1b[31;1m"
_reset = "\x1b[0m"

_LOG_DIR = str(Path.cwd() / "logs")
_LOGGER_NAME = "project_name"


class __BaseLogger:
    def __init__(self):
        self.logger = logging.getLogger(_LOGGER_NAME)
        self.logger.setLevel(logging.DEBUG)
        # Include current date in log file name
        log_file = f"{date.today().strftime('%Y-%m-%d')} - beapp.log"
        Path(_LOG_DIR).mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(f"{_LOG_DIR}/{log_file}")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def check_file_or_create(self):
        log_file = f"{date.today().strftime('%Y-%m-%d')} - beapp.log"
        try:
            # pylint: disable=consider-using-with
            open(f"logs/{log_file}", "x", encoding="utf-8")
        except FileExistsError:
            pass
        fh = logging.FileHandler(f"logs/{log_file}")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        self.logger.addHandler(fh)

    def debug(self, msg, *args):
        self.check_file_or_create()
        _msg = ""
        if args:
            _msg = f"{msg}, {args}"
        self.logger.debug(_msg)
        print(f"{_dark_grey}DEBUG: {_msg}{_reset}")

    def info(self, msg, *args):
        self.check_file_or_create()
        _msg = ""
        if args:
            _msg = f"{msg}, {args}"
        self.logger.info(_msg)
        print(f"{_grey}INFO: {_msg}{_reset}")

    def warning(self, msg, *args):
        self.check_file_or_create()
        _msg = ""
        if args:
            _msg = f"{msg}, {args}"
        self.logger.warning(_msg)
        print(f"{_yellow}WARNING: {_msg}{_reset}")

    def error(self, msg, *args):
        self.check_file_or_create()
        _msg = ""
        if args:
            _msg = f"{msg}, {args}"
        self.logger.error(_msg)
        print(f"{_red}ERROR: {_msg}{_reset}")

    def critical(self, msg, *args):
        self.check_file_or_create()
        _msg = ""
        if args:
            _msg = f"{msg}, {args}"
        self.logger.critical(_msg)
        print(f"{_bold_red}CRITICAL: {_msg}{_reset}")


logger = __BaseLogger()
