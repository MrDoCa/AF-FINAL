
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1940528498:AAGDMEWQURjlNj-SvlP4p1PRmOxCNjptadw")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", 4626470))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "d0b545107dfacaccf94de87d9732c4f1")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCT93gyGWL-CvFm3cYnrruLsurRcodXHm6PPc3Rwx3ro8kmRDJ0vfODU5Aphg-lufFNW6SaiOJWR2karwyeD3ZQ2nXhVVVPVL0hB9exQ40zzagFoqXvl7-Yjmj065ZncRM9K6pPD69r86bow4dPWhAmj7JNflG5U_kDn9BFJAW2EdcBFkPsI5F3V_QLfUAWmEJu77iwHwDrBvpjD8v2UzLYCNfniCTRe1czDeuvt7y96v1RtkOFd23BlY25WT3C687xLfWqjg1F0YfGGD57VCh2m0A81QaOseJu3u9QkVeqW6eqPcWLTq_jP9N43HzF37ZKElU73aDT-8vZkfZtotQQZySJ1wA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://second:second@cluster0.s3aor.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1730447831").split())

#Small Admins
SM_ADMIN = set(int(x) for x in os.environ.get("SM_ADMIN", "1398980025").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "no").lower()

#Should bot search for Images
PHO_SEARCH = os.environ.get("PHO_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()

#Link of the Channel
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/infinityLK/")

#Web Site Link
WEB_SITE_URL = os.environ.get("WEB_SITE_URL", "https://www.irupc.net/p/bot.html?")

#text set when User Request Subtitle
SUB_TEXT = os.environ.get("SUB_TEXT", "𝕊𝕦𝕓𝕥𝕚𝕥𝕝𝕖 ❗️ ")

# Link to File bot url before Array
BOT_URL = os.environ.get("BOT_URL", "https://t.me/SERVERinf_bot?start=")

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
