import os

API_ID = API_ID = 29691147

API_HASH = os.environ.get("API_HASH", "764d9a7ff33ebca02e985e2ceace0cfe")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6921407455:AAFrgKzZ7tYgwWxP3GsF_Ta7Dz2uWC_qOZ8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6867714531))

LOG = -1002059181631

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6867714531").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


