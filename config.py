import os

API_ID = API_ID = 29691147

API_HASH = os.environ.get("API_HASH", "764d9a7ff33ebca02e985e2ceace0cfe")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7104524100:AAEHDXfvpWSC7hmVyOCzYtBqawCiXMbYwXs")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6867714531))

LOG = -1001990245422

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


