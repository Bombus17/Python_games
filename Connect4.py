#Author:	azmathias Stuperuser Ltd
#Purpose:	Command line Connect 4 game
#
#
#TODO:		Create graphic board, track scores, replay game?, TESTING
#			check valid selection, error handling
#Extensions: Allow user to select the board size

import numpy as np

# global variables
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_1 = 1
PLAYER_2 = 2

# create matrix
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board
	
def play(board, row, selection, piece):
	board[row][selection] = piece

# check column has an emtpy space	
def isvalidlocation(board, selection):
	return board[ROW_COUNT-1][selection] == 0

def get_next_row(board, selection):
	for r in range(ROW_COUNT):
		if board[r][selection] == 0:
			return r

def flip_board(board):
	print(np.flip(board, 0))

#manually check all possible ways to win and take first instance
#better to check around the last drop....	
def win(board, piece):
	# check horizontal
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1]== piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True
	# check vertical (not working correctly for player 2)
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c]== piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True
			
	# positive diagnols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1]== piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True
	
	# negative diagnols
	for c in range(COLUMN_COUNT):
		for r in range(3,ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1]== piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
				
board = create_board()
flip_board(board)	
game_over = False
player_turn = 0
	
while not game_over:
	# Player 1 input
	if player_turn == 0:
		selection = int(input("\nPlayer 1: Make your selection (0-6):\n"))
		
		if isvalidlocation(board, selection):
			row = get_next_row(board, selection)
			play(board, row, selection, PLAYER_1)
			
			if win(board, 1):
				print("\nPLAYER 1 WINS!!!\n")
				game_over = True
	
	# Player 2 input
	else:
		selection = int(input("\nPlayer 2: Make your selection (0-6):\n"))
		
		if isvalidlocation(board, selection):
			row = get_next_row(board, selection)
			play(board, row, selection, PLAYER_2)
			
			if win(board, 2):
				print("\nPLAYER 2 WINS!!!\n")
				game_over = True
	
	flip_board(board)
	
	player_turn += 1
	player_turn = player_turn % 2
	
	

