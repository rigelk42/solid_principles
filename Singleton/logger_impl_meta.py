import logging
import threading
from abc import ABCMeta, abstractmethod


class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwds):
        with cls._lock:
            print("<SingletonMeta> in the __call__")
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwds)

        return cls._instances[cls]


class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


class MyLogger(BaseLogger):

    def __init__(self):
        print("<Logger init> Initializing logger...")
        self._logger = logging.getLogger("my_logger")
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("my_log_file.log")
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.error(message)

    def critical(self, message):
        self._logger.critical(message)


logger = MyLogger()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
print(f"logger: {logger}")
