import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24093810"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a0e8b7b84b92729cc346daaeb39a1961")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "770392298"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://officialslayer598_db_user:R9SCWbkPcShhBacb@cluster0.oyqv8ek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', true))
