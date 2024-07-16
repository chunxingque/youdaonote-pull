import logging
import sys
import os
from time import strftime, localtime


LOG_FORMAT = "%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(funcName)-10s : %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S "

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

now_time = strftime("%Y%m%d", localtime())

log_dir = os.path.join(BASE_DIR,'logs')
log_path = os.path.join(log_dir,f'pull_{now_time}.log')
print(log_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def init_logging():
    logging.basicConfig(
        handlers=[logging.FileHandler(log_path, 'a', encoding='utf-8'), logging.StreamHandler(sys.stdout)],
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT)
