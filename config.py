from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "21967614"))
API_HASH = getenv("API_HASH", "0925fb18d5910caa9782e317b7a2149a")
BOT_TOKEN = getenv("BOT_TOKEN", "6170338903:AAEYiPBOzLsuOZv5yCACadK9C11a22oYyQI")
SESSION_NAME = getenv("SESSION_NAME", "BABUItQDOnJCKhDYgOjsM0ba0ln6QQ29fnM7qJRMHJGwVPRSbA06g9QA5a4wE1MwaQSng1uzpFAv9bInWQdTjnS62NHrpMGqOsavqv6BkO9vuwBYXuZ60j64GuzHsDYxRsOUlY9dZ6YTzrggHS51PuOcVHeE5zVipn1l_y7pTFLDFfROGPy07NBISTK43cphV2j9Mi6k0igubItg9MBZqvOGHMbMYxmlV0dQQQrLRHosS7oTxBpJheCYQSPGkpvOkt8Z0auZ96H3y8erGUO0--6qzAKweL3vC8uAQ3EsFySrXiUf-boskkj2HUZCMl4CMrNtIfHNYZ8W3AWdsVnGf-IxAAAAAUYhxK4A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "BotConfectionary")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "BotConfectionarybot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ggkauyggg")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
