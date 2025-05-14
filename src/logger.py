import logging
import os
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.path.dirname(__file__), LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)
LOG_FILE_PATH = os.path.abspath(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)