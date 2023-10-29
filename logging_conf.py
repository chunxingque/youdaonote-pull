import logging
import sys

LOG_FORMAT = "%(asctime)s %(levelname)s %(processName)s-%(threadName)s-%(thread)d %(filename)s:%(lineno)d %(funcName)-10s : %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S "


def init_logging():
    logging.basicConfig(
        handlers=[logging.FileHandler('pull.log', 'a', encoding='utf-8'), logging.StreamHandler(sys.stdout)],
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT)
