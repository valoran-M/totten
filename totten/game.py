from discord import Message

from games.bingo import Bingo
from games.capital import Capital
from games.pokemon import Pokemon
from games.RPS import RPS

class Game():
    """
    """
    def __init__(self, message, prefix):
        commande = message.content.split(' ')
        self.game = commande[1]
        self.message = message        

    async def launch(self, client):
        if(self.game == "bingo"):
            bingo = Bingo(self.message)
            await bingo.launch(client)
        if(self.game == "capital"):
            capital = Capital(self.message)
            await capital.launch(client)
        if(self.game == "pokemon"):
            pokemon = Pokemon(self.message)
            await pokemon.launch(client)
        if(self.game == "rps"):
            rps = RPS(self.message)
            await rps.launch(client)
        return   
    