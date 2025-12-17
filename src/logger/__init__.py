import logging
import os, sys
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamp for the log file name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log" # file - log_2023-06-15-12-30-45.log


log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(
    filename=log_file_path,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)