import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5411632547:AAGdJ5vKV_R7696oVi4eJ7BX2M6sP5DMxEc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "1669750"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0f53ee8c576281995d621194aec588d8")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001946672954"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "831370530 1852823985"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://abhyqmgp:xWR8ugCjF9fkgaMNtupG4d2uWskXuSzQ@satao.db.elephantsql.com/abhyqmgp")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "╔┓┏╦━━╦┓╔┓╔━━-\n║┗┛║┗━╣┃║┃║ ^ ^ ✦\n║┏┓║┏━╣┗╣┗╣╰╯║\n╚┛┗╩━━╩━╩━╩━━╝\n\n\n<b>Hello {first}\nI am a bot which will provide you files instantly which are shared in @Kan_Serial and @SB_SERIALS </b>\n\n⚠Kindly Please join my channel - Serial Adda and Kannada Channels Link / ದಯವಿಟ್ಟು ನನ್ನನ್ನು ಬಳಸಲು ಚಾನಲ್‌ಗೆ ಸೇರಿಕೊಳ್ಳಿ⚠")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "718979130").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Kindly Please join my channel - @Kan_Serial and @SB_SERIALS / ದಯವಿಟ್ಟು ನನ್ನನ್ನು ಬಳಸಲು ಚಾನಲ್‌ಗೆ ಸೇರಿಕೊಳ್ಳಿ - @Kan_Serial and @SB_SERIALS </b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! Only sudo users can use me!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

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
