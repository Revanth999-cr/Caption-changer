from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

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

app.run()
