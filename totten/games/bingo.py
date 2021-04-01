from discord import Message, Client, File
from random import randint

class Bingo():
    """
	"""

    def __init__(self, message):
        commande = message.content.split(' ')
        self.number = int(commande[1])
        self.indic = True if len(commande) == 3 and commande[2] == 'indic' else False
        self.inc = randint(1, self.number)
        self.channel = message.channel

    async def launch(self, client):
        def is_correct(m):
            return m.channel == self.channel and m.content.isdigit()

        await self.channel.send(f"Le bingo commence ! Trouve le nombre entre 1 et {self.number}")
        rep = -1
        print(self.inc)
        while rep != self.inc:
            guess = await client.wait_for(event='message', check=is_correct)
            rep = int(guess.content)
            if(rep) > self.inc and self.indic:
                await self.channel.send("Ton nombre est trop grand")
            if(rep) < self.inc and self.indic:
                await self.channel.send("Ton nombre est trop petit")
        await self.channel.send(
            f"Bravo, le nombre était {self.inc}", file=File("images/toutou.png")
        )
