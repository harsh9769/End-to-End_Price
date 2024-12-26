import logging
import os
import sys

log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory for logs
log_dir = "logs"

# File path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)  # Log to console
    ]
)

# Create a logger
logger = logging.getLogger("house_reg_logger")

# Example log message
logger.info("Logging setup successful.")
