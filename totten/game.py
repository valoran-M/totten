from discord import Message

from games.bingo import Bingo
from games.capital import Capital

class Game():
    """
    """
    def __init__(self, message, prefix):
        commande = message.content.split(' ')
        self.game = commande[0][len(prefix):]
        self.message = message

    async def launch(self, client):
        if(self.game == "bingo"):
            bingo = Bingo(self.message)
            await bingo.launch(client)
        if(self.game == "capital"):
            capital = Capital(self.message)
            await capital.launch(client)
        return   
    