# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

corrc_letter = []
wrong_letter = []
entrada = []

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		
	# Método para adivinhar a letra
	def guess(self, letter):
		self.letter = letter
		for each in self.word:
			if each == self.letter:
				corrc_letter.append(letter)
		if letter in self.word:
			return
		else:
			wrong_letter.append(letter)
	
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(wrong_letter) == 6:
			return True
		elif len(corrc_letter) == len(self.word):
			return True
		else:
			return False
	
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if len(corrc_letter) == len(self.word):
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self, hidden_word):
		self.hidden_word = hidden_word
		for letter in self.word:
			hidden_word += "_"
		print(hidden_word)
		
	# Método para checar o status do game e imprimir o board na tela
	def show_game_status(self):
		print(board[len(wrong_letter)])
		print("Palavra: "), self.hide_word()
		print("Letras Erradas: ", wrong_letter)
		print("Letras Corretas: ", corrc_letter)	



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while game.hangman_over == False:
		game.show_game_status()
	#	print("Palavra: "), game.hide_word()
	#	print("Letras Erradas: ", wrong_letter)
	#	print("Letras Corretas: ", corrc_letter)
		game.guess(input("Digite uma letra: "))
	
	



	# Verifica o status do jogo
	game.show_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
