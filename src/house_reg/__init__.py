import logging 
import os

log_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"

log_filepath=os.path.join(log_dir,"running_logs.log")

os.makedirs(log_filepath,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(log_filepath)
    ]
)

logger=logging.getLogger("house_reg_logger")
