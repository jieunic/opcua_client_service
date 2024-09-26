import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from svcEngine.utils import root, file_execution as exec

env = "svcEngine/setup.env"
service_log_path = f"{root.dir()}{exec.Env.get(env, "LOG_SERVICES")}"
transaction_log_path = f"{root.dir()}{exec.Env.get(env, "LOG_TRANSACTION")}"

def get_log_filename(log_path):
    current_date = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(log_path, f'log_{current_date}.log')

service_logger = logging.getLogger('service')
service_handler = RotatingFileHandler(get_log_filename(service_log_path), maxBytes=50*1024*1024, backupCount=5)
service_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
service_handler.setFormatter(service_formatter)
service_logger.addHandler(service_handler)
service_logger.setLevel(logging.DEBUG)

transaction_logger = logging.getLogger('transaction')
transaction_handler = RotatingFileHandler(get_log_filename(transaction_log_path), maxBytes=50*1024*1024, backupCount=5)
transaction_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
transaction_handler.setFormatter(transaction_formatter)
transaction_logger.addHandler(transaction_handler)
transaction_logger.setLevel(logging.INFO)