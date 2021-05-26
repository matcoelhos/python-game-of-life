import random
import time
import os

board = []
lines = 40
columns = 119

def printb(board):
	for i in range(lines):
		for j in range(columns):
			if board[i][j] == 1:
				print(chr(9608), end='')
				print(chr(9608), end='')
			else:
				print(' ', end='')
				print(' ', end='')
		print()

def next_board():
	global board
	nboard = board.copy()
	for i in range(lines):
		for j in range(columns):
			neighbors = []
			value = board[i][j]
			for k in range(i-1,i+2):
				for l in range(j-1,j+2):
					if (k != i and l != j and k >= 0 and l >= 0 and k < lines and l < columns):
						neighbors.append(board[k][l])
						
			if (value == 1 and sum(neighbors)<2):
				nboard[i][j] = 0
			if (value == 1 and sum(neighbors)>3):
				nboard[i][j] = 0
			if (value == 0 and sum(neighbors)==3):
				nboard[i][j] = 1
			if (value == 1 and (sum(neighbors)==2 or sum(neighbors)==3)):
				nboard[i][j] = 1
	return nboard


for i in range(lines):
	line = []
	for j in range(columns):
		if random.random() < 0.60:
			line.append(1)
		else:
			line.append(0)
	board.append(line)

while(True):
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		printb(board)
		board = next_board().copy()
		time.sleep(0.1)
	except:
		print()
		print('Interrupted.')
		break
