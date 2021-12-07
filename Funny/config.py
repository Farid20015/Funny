import telegram
import os

class Config(object):
    DORY_BOT_TOKEN = "2101580139:AAFNH2lc3lhl-CjuAn4zcc7yQOkpYMVGgds" 
    dorybot = telegram.Bot(token=DORY_BOT_TOKEN)
    BOT_TOKEN=os.environ["BOT_TOKEN"]
    APP_ID=int(os.environ["APP_ID"])
    API_HASH=os.environ["API_HASH"]
    AWHT_ID="Misto"
    TG_ID=os.environ["TG_ID"]
    LOGGER_CHANNEL={1:-1001504042737,2:-1001538256096,"bug":-1001576680163}

