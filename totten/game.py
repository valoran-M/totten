from discord import Message

class Game():
    """
    """
    def __init__(self, message, prefix):
        commande = message.content.split(' ')
        self.game = commande[0][len(prefix):]

    def launch(self):
        if(self.game == "bingo"):
            print("a")
        return   
    