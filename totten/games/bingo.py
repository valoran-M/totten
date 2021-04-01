from discord import Message, Client, File
from random import randint


class Bingo:
    """
	"""

    def __init__(self, message):
        commande = message.content.split(" ")
        self.number = int(commande[1])
        self.indic = True if len(commande) == 3 and commande[2] == "indic" else False
        self.inc = randint(1, self.number)
        self.channel = message.channel

    async def launch(self, client):
        def is_correct(m):
            return m.channel == self.channel and m.content.isdigit()

        await self.channel.send(
            f"The bingo begins ! Find a number between 1 and {self.number}"
        )
        rep = -1
        print(self.inc)
        while rep != self.inc:
            guess = await client.wait_for(event="message", check=is_correct)
            rep = int(guess.content)
            if (rep) > self.inc and self.indic:
                #await self.channel.send("Your number is to big")
                await guess.add_reaction('⬇')
            if (rep) < self.inc and self.indic:
                #await self.channel.send("Your number is to small")
                await guess.add_reaction('⬆')
        await self.channel.send(
            f"{guess.author.mention}\n🎉Well done, the number was {self.inc} 🎉"
        )
