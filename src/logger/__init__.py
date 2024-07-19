import os
import logging
from datetime import datetime

LOG_DIR = "/home/avaxpro/Desktop/prediction/logs"  # Adjust as per your desired location
os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


'''import logging

# Basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')'''




