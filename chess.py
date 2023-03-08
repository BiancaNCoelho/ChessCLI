# chess.py

import numpy as np

col = ['a','b','c','d','e','f','g','h']
black = ['r','p','n','b','q','k']
white = ['R','P','N','B','Q','K']

class Game():
	"""
		Class Game.
	"""
	def __init__(self):
		self.board = Board()
		self.pieces = Piece()
		self.player1 = Player('white',1)
		self.player2 = Player('black',2)
		self.turn = True
			
	def promotion(self):
		# Promotes the Pawn
		pass
	
	def is_valid_move(move_from,move_to,piece,target):

		if piece == 'p' or piece == 'P':
			return self.pieces.is_valid_move_pawn(move_from,move_to,piece,target)
		if piece == 'b' or piece == 'B':
			return self.pieces.is_valid_move_bishop(move_from,move_to,piece,target)
		if piece == 'k' or piece == 'K':
			return self.pieces.is_valid_move_king(move_from,move_to,piece,target)
		if piece == 'q' or piece == 'Q':
			return self.pieces.is_valid_move_queen(move_from,move_to,piece,target)
		if piece == 'r' or piece == 'R':
			return self.pieces.is_valid_move_rook(move_from,move_to,piece,target)
		if piece == 'n' or piece == 'N':
			return self.pieces.is_valid_move_knight(move_from,move_to,piece,target)
		
		return False
		
	def move(self,move_from,move_to):
		
		for i in range(col):
			if move_from[0] == col[i]:
				num_from = i
			if move_to[0] == col[i]:
				num_to = i
		
		if self.board[int(move_from[1])][num_from] == ' ':
			print(f'Não há uma peça nesta posição.')
			return
		
		piece = self.board[int(move_from[1])][num_from]
		
		if self.check_piece_color(piece):
			print(f'4: Não é a sua peça')
			return
		
		target = self.board[int(move_to[1])][num_to]
		if piece.isupper() and target.isupper():
			print(f"5: Não pode comer sua própria peça.")
			return
		if piece.islower() and target.islower():
			print(f'5: Não pode comer sua própria peça')
			return
		
		if self.is_valid_move(move_from,move_to,self.board.get_board()):
		
			if target == ' ':
				self.board[int(move_from[1])][num_from]	= ' ' 
				self.board[int(move_to[1])][num_to] = piece						
			if target in black or target in white:
				self.board[int(move_from[1])][num_from]	= ' ' 
				self.board[int(move_to[1])][num_to] = piece
				if piece in black:
					self.player1.dead_pieces(target)
				if piece in white:
					self.player2.dead_pieces(target)

			if piece in white:
				self.turn = True
			if piece in black:
				self.turn = False 
		else:
			print(f'7: Movimento inválido.')
			return
	
	def check_piece_color(self,piece):
		if self.turn:
			if piece not in white:
				return True
		else:
			if piece not in black:
				return True
		return False
		
	def transform_input(self,move):
		m = move.split(' ')
		m_from = list(m[0])
		m_to = list(m[1])
		
		try:
			if int(m_from[1]) < 1 or int(m_from[1]) > 8:
				print(f"1: Não é um número entre 1 - 8.")
			if m_from[0] < 'a' or  m_from[0] > 'h':
				print(f'2: Não é uma letra entre a - h')
			return m_from, m_to
		except:
			print(f"3: {m_from} não está no formato certo: [letra][número]") 
			return None
		try:
			if int(m_to[1]) < 1 or int(m_to[1]) > 8:
				print(f"1: Não é um número entre 1 - 8.")
			if m_to[0] < 'a' or  m_to[0] > 'h':
				print(f'2: Não é uma letra entre a - h')
			return m_from, m_to
		except:
			print(f"3: {m_to} não está no formato certo: [letra][número]") 
			return None
		
		return None

class Board():
	"""
		Board Class.
	"""
	def __init__(self):
		self.line = [' ','a','b','c','d','e','f','g','h']
		self.column = [['8'],['7'],['6'],['5'],['4'],['3'],['2'],['1']]
		self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
			      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                              ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
	def print_board(self):
		boardP= np.hstack((self.column,self.board))
		for row in boardP:
			print(' '.join(row))
		for i in self.line:
			print(i, end = ' ')
		print(f'\n')
	
	def get_board(self):
		return self.board

class Player():
	def __init__(self, color, pNumber):
		self.color = color
		self.pNumber = pNumber
		self.dead_pieces = []
	
	def getPlayer(self):
		return {'color': self.color, 'pNumber': self.pNumber}

	def dead_pieces(self, piece):
		self.dead_pieces.append(piece)
		
	def list_deadpieces(self):
		for i in self.dead_pieces:
			print(f'{i}: {dead_pieces[i]}')
	
	def getDead_pieces(self):
		return self.dead_pieces

class Piece():
		
	def is_valid_move_rook(move_from,move_to,board):
		if int(move_from[1]) == int(move_to[1]) or move_from[0] == move_to[0]:
			return check_updown(move_from, move_to,board)
		print(f'8: Movimento inválido.')
		return False
		
	def is_valid_move_bishop(move_from,move_to,board):
		pass

	def is_valid_move_queen(move_from,move_to,board):
		pass
	
	def is_valid_move_king(move_from,move_to,board):
		pass

	def is_valid_move_knight(move_from,move_to,board):
		
		for
		
		if abs(int(move_from[0]) - int(move_to[0])) == 2 and abs(int(move_from[1]) - int(move_to[1])) == 1:
			return True			
		if abs(int(move_from[0]) - int(move_to[0])) == 2 and abs(int(move_from[1]) - int(move_to[1])) == 1:
			return False
		
		print(f'8: Movimento inválido.')
		return False

	def is_valid_move_pawn(move_from,move_to,board):
		pass
	
	def check_updown(move_from, move_to, board)
		if move_from[1] == move_to[1]:
			smaller_y = int(move_from[0]) if int(move_from[0]) < int(move_to[0]) else int(move_to[0])
			bigger_y =  int(move_from[0]) if int(move_from[0]) > int(move_to[0]) else int(move_to[0])
			
			for i in range(smaller_y +1, bigger_y):
				if board[int(move_from[1])][i] != ' ':
					print(f'13: Caminho bloqueado.')
					return False
			return True
		else:
			smaller_x = int(move_from[1]) if int(move_from[1]) < int(move_to[1]) else int(move_to[1])
			bigger_x =  int(move_from[1]) if int(move_from[1]) > int(move_to[1]) else int(move_to[1])
			
			for i in range(smaller_x +1, bigger_x):
				if board[i][int(move_from[0])] != ' ':
					print(f'13: Caminho bloqueado.')
					return False
			return True
			
if __name__ == "__main__":
	chess = Game()
	chess.board.print_board()
	
	
	while True:
		move = input("Sua jogada - de para - (exemplo: e2 e4): ")		
		
		move_from, move_to = chess.transform_input(move)
		
		chess.move(move_from,move_to)
		
		chess.board.print_board()
