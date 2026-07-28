import os

# Telegram API
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# Userbot String Session
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Optional
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
