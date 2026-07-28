import os
import threading
from flask import Flask
from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

# ---------------- Web Server ---------------- #

web = Flask(__name__)

@web.route("/")
def home():
    return "Bold Caption Userbot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# ---------------- Userbot ---------------- #

app = Client(
    "BoldCaptionBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
bold = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
table = str.maketrans(normal, bold)

def to_bold(text):
    if not text:
        return ""
    return text.translate(table)

@app.on_message(filters.channel)
async def channel_post(client, message):
    try:
        if message.caption:
            await message.edit_caption(to_bold(message.caption))
        elif message.text:
            await message.edit_text(to_bold(message.text))
    except Exception as e:
        print(e)

print("✅ Bold Caption Userbot Started")
app.run()
