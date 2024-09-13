# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22439323"))
API_HASH = getenv("API_HASH", "e0e203c8be2c2c58b04d0c59fc82f507")
BOT_TOKEN = getenv("BOT_TOKEN", "7486518554:AAHiJqGksomQanRhrihPOj4aGSAm0QkACtQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7328902365").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://singhalparul98:fCxWD0p8SAIiLaGP@clustersrcb.thgqk.mongodb.net/?retryWrites=true&w=majority&appName=Clustersrcb")
LOG_GROUP = getenv("LOG_GROUP", "-1002204157533")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002204157533"))
