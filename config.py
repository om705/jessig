import os
from os import getenv

API_ID = getenv("API_ID", "26115463")

API_HASH = getenv("API_HASH", "054557eca362bba15769130a5fadf0de")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6956215581:AAF-vMdygW-I0jpf34amaAZYttJqzKO5QZc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

sudo_group = -1002022753943
sudo_user = 6631088681
log_channel = -1002033194166

# try:
#     ADMINS=[]
#     for x in (os.environ.get("ADMINS", "6631088681 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
#         ADMINS.append(int(x))
# except ValueError:
#         raise Exception("Your Admins list does not contain valid integers.")
# ADMINS.append(OWNER)


