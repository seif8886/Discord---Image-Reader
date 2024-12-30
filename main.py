import discord
from os import environ
from dotenv import load_dotenv
from imagereader import *
from messages import *


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.author.bot:
            # checking message content
            if len(message.attachments) > 0:
                image_statement = read_image_text(message.attachments[0].url)
                if not image_statement == "Nothing":
                    messages_agenda_dict = get_messages_agenda_dict()
                    await message.reply(messages_agenda_dict[image_statement]["reply_message"])


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

load_dotenv()

token = environ["TOKEN"]

client.run(token)
