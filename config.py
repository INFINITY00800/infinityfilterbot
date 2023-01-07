
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5878908265:AAFozSkiK_y90P-prlOEp4VfL4HiVpdERrk")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", " 10312880"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", " a3453ab68ddebf41f9954cea16044583")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC8_kBDSnWz55wT91zgrBLyUqyu4pE9ubnn3YwsbDW857LK17rZHbwX_jPH-HWkOZr6lhTaDT3sZax56YgeZD5ieD3E-nn3w62tJurB78YaCR_l_TE1e1ad3fCh79DSamnwb8mYnV0fS0yzXmr-kiZXeOq61MxMvHArm32LNL66iNQ3WJVV8yXoDFlNSwO_75MG878Z5hEuVyVXuHnQNKmE3iF4TYk7ZXQpfvDC5FFf8jRQq4Og2teHNmCb7Lqz6RG7sjZsqSfqepir2thzKlfkakJ5ktrWi_cxTss2AkAF6a2-N0hJ-s9AXUmU1dRrc7XzkX6xtYfn3rm_jewGINDKAAAAATB7Fb4A")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001779529838")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
