import logging 
import os
import sys

log_dir="[%(asctime)s-%(levelname)s-%(module)s-%(message)s]"
logdir="logs"
logfilepath=os.path.join(logdir,"running_logs.log")
os.makedirs(logdir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_dir,
    handlers=[
        logging.FileHandler(logfilepath),
        logging.StreamHandler(sys.stdout)  # Output to console as well.
    ]
)

logger=logging.getLogger("cnnclassification")