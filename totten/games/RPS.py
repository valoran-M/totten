from discord import Message, Client, File
from random import randint
from time import time

class RPS:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        #tab = ['Rock','Paper','Scissors']
        tab = ['🪨','📰','✂']
        self.botplay = tab[randint(0,2)].lower()

    async def launch(self, client):
        
        def check(reaction, user):
            return user == self.author and (str(reaction.emoji) == '🪨' or str(reaction.emoji) == '📰' or str(reaction.emoji) == '✂')
        
        await self.channel.send("Rock, Paper or Scissors")
        message = await client.wait_for(event="reaction_add", check=check)
        print('ok')
        #guess = message.content.lower()
        guess = str(reaction.emoji)

        if guess == self.botplay:
            await self.channel.send(f"{message.author.mention}\nI have chosen {self.botplay} so it's draw ")
            return
        if (guess == 'rock' and self.botplay == 'paper') or (guess == 'paper' and self.botplay == 'scissors') or (guess == 'scissors' and self.botplay == 'rock'):
            await self.channel.send(f"{message.author.mention}\nSorry, I have chosen {self.botplay} so you lost ")
        else :
            await self.channel.send(f"{message.author.mention}\nGG, I have chosen {self.botplay} so you won ")