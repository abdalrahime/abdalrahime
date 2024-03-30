import os
import pyrogram
import openai
from pyrogram.filters import private
from config import Config
from handlers.message_handler
 import MessageHandler
# Initialize the Pyrogram client
app = pyrogram.Client(
session_name=”my_bot”,
api_id=Config.API_ID,
api_hash=Config.API_HASH,
bot_token=Config.BOT_TOKEN
 )

# Initialize the OpenAI API
openai.api_key = Config.OPENAI_API_KEY

# Initialize the message handler
message_handler = MessageHandler(openai.api_key)
 # Register the message handler with the “private” filter app.on_message(message_handler.handle, filters=private
 )

# Run the bot
app.run()
