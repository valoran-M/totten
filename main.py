from discord import Intents
from src.bot import Bot
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    Bot_intents = Intents.none()
    Bot_intents.guilds = True
    Bot_intents.emojis = True
    Bot_intents.messages = True
    Bot_intents.guild_messages = True
    Bot_intents.dm_messages = True
    Bot_intents.reactions = True
    Bot_intents.guild_reactions = True
    Bot_intents.dm_reactions = True
    Totten = Bot(Bot_intents)
    Totten.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    main()
