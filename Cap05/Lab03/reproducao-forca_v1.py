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

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		
	# Método para adivinhar a letra
	def guess(self, letter):
		self.letter = letter
		for each in self.word:
			if each == self.letter and letter not in corrc_letter:
				corrc_letter.append(letter)
		if letter in self.word:
			return
		elif letter not in self.word and letter not in wrong_letter:
			wrong_letter.append(letter)
		else:
			return False
		return True
	
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.hangman_won() or len(wrong_letter) == 6:
			return True
		else:
			return False
	
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		hidden_word = ''
		for letter in self.word:
			if letter in corrc_letter:
				hidden_word += letter
			else:
				hidden_word += '_'
		return hidden_word
		
	# Método para checar o status do game e imprimir o board na tela
	def show_game_status(self):
		print(board[len(wrong_letter)])
		print('Palavra: ' + self.hide_word())
		print('Letras Erradas: ', wrong_letter)
		print('Letras Corretas: ', corrc_letter)	


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Loop while, enquanto o jogo não tiver terminado, print do status, solicita uma letra e 
	# faz a leitura do caracter, depois retorna ao loop até que o jogo tenha terminado
	while game.hangman_over() == False:
		game.show_game_status()
		game.guess(input("Digite uma letra: "))
	
	# Verifica o status do jogo <--- desnecessario 
	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		game.show_game_status()
		print ('\nParabéns! Você venceu!!')
	else:
		game.show_game_status()
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
