import pyrogram
import openai
class MessageHandler:
def __init__(self, openai_api_key):
self.openai_api_key = openai_api_key
def handle(self, client, message):
# Ignore messages sent by the bot itself
if message.from_user.is_bot:
return
# Generate a response using the OpenAI API
response = self.generate_response(message.text)
# Send the response back to the user
client.send_message(
chat_id=message.chat.id,
text=response
)
def generate_response(self, input_text):
# Set up the OpenAI API client
openai.api_key = self.openai_api_key
completions = openai.Completion.create(
engine=”davinci”,
prompt=input_text,
max_tokens=60,
n=1,
stop=None,
temperature=0.7,
)
# Extract the response from the OpenAI API result
response = completions.choices[0].text.strip()
return response
