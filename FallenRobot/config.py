class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 14831989
    API_HASH = "75156d6ac13293f935e50f4ec3a6f243"

    CASH_API_KEY = "omg"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://database_uri_user:dFAywDlRiBPrNXOlR4D5Yc7MrmFZSaVu@dpg-cej9fqla4991ihm77mgg-a/database_uri"
    EVENT_LOGS = (-1001558733714)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://foxbot:<an12if..>@cluster0.cweve3x.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/31ee1d1cce339094e2c93.mp4"

    SUPPORT_CHAT = "TeamFoxBots"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "1060722149:AAEus2ZKZcH72RoT_9qVwBQc6AzAQ_kc3wM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "6E9UG7JETLHA"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 820596651  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [912095781,1105084940,1205330781,862852632,1378572693,999873027,644412009,865643300,1769085034,1833664399,1721373213,1276998600,1555340229,1647428346,1476128450,1734396873,2019529859,1926765024,5574601095]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
