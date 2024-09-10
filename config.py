## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "FTM")

if str(getenv("STRING_SESSION2")).strip() == "FTM1":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "FTM3":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "FTM4":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "FTM5":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "7449988437:AAFFxdpVdedmUt0pcX0YDBrbC2jbnYwTq9E")
BOT_NAME = getenv("BOT_NAME", "FTM PLAYER")

API_ID = int(getenv("API_ID", "28776072"))
API_HASH = getenv("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_NAME = getenv("OWNER_NAME", "╚» 𝔽𝕋𝕄 𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝔼ℝ«╝")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ftmdeveloper")
ALIVE_NAME = getenv("ALIVE_NAME", "FTM")
BOT_USERNAME = getenv("BOT_USERNAME", "ftmplayerbot")
OWNER_ID = getenv("OWNER_ID", "7042535787")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FTM_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FTM MOVIES WORLD")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ftmmovieworldofficial")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7042535787").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
