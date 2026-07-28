from pyrogram import Client, filters

API_ID = 123456          # Replace
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client(
    "BoldCaptionBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
bold = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
table = str.maketrans(normal, bold)

def to_bold(text):
    return text.translate(table)

@app.on_message(filters.channel)
async def channel_post(client, message):
    if not message.caption:
        return

    caption = to_bold(message.caption)

    try:
        await message.copy(
            chat_id=message.chat.id,
            caption=caption
        )
    except Exception as e:
        print(e)

app.run()
