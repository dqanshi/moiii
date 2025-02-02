import json
import os



def get_user_list(config, key):
    with open("{}/FallenRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]




class Config(object):
    LOGGER = True




  # Get this value from my.telegram.org/apps
    API_ID = 1207230
    API_HASH = "b89d2ee79c70c5fbf9299e34f16e27e0"

    CASH_API_KEY = "omg"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://anshif_user:l7wiLk93MEMFq7gmvAhPJEw7L0gYroN7@dpg-cu5dvmbtq21c73e01b2g-a.oregon-postgres.render.com/anshif"
    EVENT_LOGS = (-1001558733714)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Dqanshi:an12if@cluster0.0gt4d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/31ee1d1cce339094e2c93.mp4"

    SUPPORT_CHAT = "dbots_supportchat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "1060722149:AAHU02zRerIJZwFX0lwVvJRbZIs-tt_O3-E"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "6E9UG7JETLHA"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 820596651  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1721373213,912095781,1105084940,1205330781,862852632,999873027,644412009,865643300,1769085034,1833664399,1276998600,1555340229,1647428346,1476128450,1734396873,2019529859,1926765024,5574601095]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math","chatbot" ]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (1)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
