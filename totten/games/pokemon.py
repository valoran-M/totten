from discord import Message, Client, File
from random import randint
import csv

class Pokemon:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author
        f = open("images/pokemonTri.csv","r")
        table = list(csv.reader(f, delimiter=','))
        f.close()
        n = randint(1,len(table))
        self.pokemon = table[n]
        self.pokemon = self.pokemon[0] + '.png'
        self.chemin = "images/images/" + self.pokemon

    async def launch(self, client):
        
        await self.channel.send(f"{self.pokemon} : ")
        await self.channel.send(file=File(self.chemin))