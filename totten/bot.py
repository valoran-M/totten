import discord
import datetime

from game import Game

class Bot(discord.Client):
    def __init__(self, Myintents):
        discord.Client.__init__(self, intents=Myintents)

    async def on_ready(self):
        """
        event when the bot is ready

        Parameters
        ----------

        Return
        ------
        None
        """
        print('Load')
        self.__guild_suport = self.get_guild(820416618101735424)
        self.__channel_logs = self.__guild_suport.get_channel(820417825072087112)

        date = datetime.datetime.now()
        embedVar = discord.Embed(
            title="Ready",
            description=f"Logged as {self.user}",
            color=0x00FF00,
            timestamp=date,
        )
        await self.__channel_logs.send(embed=embedVar)
        await self.change_presence(activity=discord.Game(name="tt?help for doc"))

    async def on_resumed(self):
        """
        event when the bot was reconected

        Parameters
        ----------
        
        Return
        ------
        None
        """
        date = datetime.datetime.now()
        embedVar = discord.Embed(
            title="Resume",
            description=f"Logged as {self.user}",
            color=0x0000FF,
            timestamp=date,
        )
        await self.__channel_logs.send(embed=embedVar)

    async def on_message(self, message):
        """
        event when the bot detecte new message

        Paramaters
        ----------
        message : discord.Message
            message recive
        
        Return
        ------
        None
        """
        if(message.content.startswith("tt?play")):
            if len(message.content.split(' ')) < 2:
                await message.channel.send(f"{message.author.mention}\nI do not have a game in parameter")
                return
            game = Game(message, "tt?")
            await game.launch(self)