from discord import Message, Client, File
from random import randint
import csv

class Capital:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        f = open("images/concap.csv","r")
        table = list(csv.reader(f, delimiter=','))
        f.close()
        n = randint(1,len(table))
        pays = table[n]
        self.nom = pays[0]
        self.capitale = pays[1]

    async def launch(self, client):
        def is_correct(m):
            return m.channel == self.channel

        await self.channel.send(
            f"What is the capital of : {self.nom} ? "
        )
        print(self.capitale)
        guess = await client.wait_for(event="message", check=is_correct)
        if guess == self.capitale:
            await self.channel.send(
                f"{guess.author.mention}\n🎉Well done, the capital was {self.capitale}🎉"
            )
        else:
            await self.channel.send(
                f"{guess.author.mention}\nSorry, the capital was {self.capitale}"
            )

