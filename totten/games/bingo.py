from discord import Message

class Bingo():
    """
    """
    def __init__(message):
        commande = message.split(' ')

    
    def launch():
        number = int(message.content.split()[1])

		def is_correct(m):
			return m.channel == message.channel and m.content.isdigit()

		await message.channel.send(f"Le bingo commence ! Trouve le nombre entre 1 et {number}")
		n = randint(1,number)
		rep = -1
		print(n)
		while rep != n:
			guess = await self.wait_for('message', check=is_correct)
			rep = int(guess.content)
		await message.channel.send(f'Bravo, le nombre était {n}')
		await message.channel.send(file=discord.File('toutou.png'))

