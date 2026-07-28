import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Optional
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
