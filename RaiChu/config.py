## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQF33hMAghzlbSup4IejYDhVYFd8LC4b-qQnY2-r7a2tXq3RHErIo_6I7T_sQEf92ZCQOa9ON20WLoFXKbH7UCxcYJJHO5idnxbFb86vGeDVPk_I6B9xp9MZtK9Z3jJEbWxsI0bWo8WRN15zuTqla5RSD4sFMAZkSHvNipQVpbaEULmV23sljdl1_zKwtPzwpm8VO65D-KXw669Qjgo6_q_XyhFn7LppHPb6XpPEA2NDoIwTDYah2k_kJv92jKxiVXWUgZzbz2WWVrnohzIXCHSGhAG4QwQRk8X3GY3BlgaIsknZkdLs-x50VmxSFzeIeqXFoQPgwmGq0MpesvaNRcmUefsExAAAAAFTbVL_AA
")
BOT_TOKEN = getenv("BOT_TOKEN", "5819661777:AAENWaLREb9nAIHKaOKZ2SA7TPRHQXP0ipI5819661777:AAENWaLREb9nAIHKaOKZ2SA7TPRHQXP0ipI")
BOT_NAME = getenv("BOT_NAME", "LVIS")
API_ID = int(getenv("API_ID", "24632851
"))
API_HASH = getenv("API_HASH", "dcd3085533f9df358b6795a06ab3de1e
")
OWNER_NAME = getenv("OWNER_NAME", "MOCA")
ALIVE_NAME = getenv("ALIVE_NAME", "MOCA")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "ne_2a")
BOT_USERNAME = getenv("BOT_USERNAME", "Livs_robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ㅤ˹XD ✘ ᴀꜱꜱɪꜱᴛᴀɴᴛ​˼1̷")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "XD_AREA_51")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "X_UPDATE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5643521137
").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://t.me/X_UPDATE/13")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sappola/music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
