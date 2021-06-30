import random

#Minesweeper Mode: Easy, Mines: 10, Board: 9x9


#main vars
running = True
mines = 10
board_width = 9
board_height = 9


#initialize blank boards
displayed_board = [["-" for i in range(board_height)] for j in range(board_width)]
real_board = [["-" for i in range(board_height)] for j in range(board_width)]

#################################################################################
#counts the adjacent mines and fills real_board with the value
def count_adjacent_mines(row, column):
	value = 0

	####################################################
	#left side boarder
	if row == 0:
		#top left corner
		if column == 0:
			#east
			if real_board[row+1][column] == "*":
				value += 1
			#southeast
			if real_board[row+1][column+1] == "*":
				value += 1
			#south
			if real_board[row][column+1] == "*":
				value += 1

		#bottom left corner
		elif column == 8:
			#east
			if real_board[row+1][column] == "*":
				value += 1
			#northeast
			if real_board[row+1][column-1] == "*":
				value += 1
			#north
			if real_board[row][column-1] == "*":
				value += 1

		#not corner left side
		else:
			#north
			if real_board[row][column-1] == "*":
				value += 1
			#northeast
			if real_board[row+1][column-1] == "*":
				value += 1
			#east
			if real_board[row+1][column] == "*":
				value += 1
			#southeast
			if real_board[row+1][column+1] == "*":
				value += 1
			#south
			if real_board[row][column+1] == "*":
				value += 1

	####################################################
	#right side boarder
	elif row == 8:
		#top right corner
		if column == 0:
			#west
			if real_board[row-1][column] == "*":
				value += 1
			#southwest
			if real_board[row-1][column+1] == "*":
				value += 1
			#south
			if real_board[row][column+1] == "*":
				value += 1

		#bottom right corner
		elif column == 8:
			#west
			if real_board[row-1][column] == "*":
				value += 1
			#northwest
			if real_board[row-1][column-1] == "*":
				value += 1
			#north
			if real_board[row][column-1] == "*":
				value += 1

		#not corner right side
		else:
			#north
			if real_board[row][column-1] == "*":
				value += 1
			#northwest
			if real_board[row-1][column-1] == "*":
				value += 1
			#west
			if real_board[row-1][column] == "*":
				value += 1
			#southwest
			if real_board[row-1][column+1] == "*":
				value += 1
			#south
			if real_board[row][column+1] == "*":
				value += 1

	####################################################
	#top side boarder
	elif column == 0:
		#east
		if real_board[row+1][column] == "*":
			value += 1
		#southeast
		if real_board[row+1][column+1] == "*":
			value += 1
		#south
		if real_board[row][column+1] == "*":
			value += 1
		#southwest
		if real_board[row-1][column+1] == "*":
			value += 1
		#west
		if real_board[row-1][column] == "*":
			value += 1

	####################################################
	#bottom side boarder
	elif column == 8:
		#east
		if real_board[row+1][column] == "*":
			value += 1
		#northeast
		if real_board[row+1][column-1] == "*":
			value += 1
		#north
		if real_board[row][column-1] == "*":
			value += 1
		#northwest
		if real_board[row-1][column-1] == "*":
			value += 1
		#west
		if real_board[row-1][column] == "*":
			value += 1

	####################################################
	#not outer edge (perimeter) of the board
	else:
		#north
		if real_board[row][column-1] == "*":
			value += 1
		#northeast
		if real_board[row+1][column-1] == "*":
			value += 1
		#east
		if real_board[row+1][column] == "*":
			value += 1
		#southeast
		if real_board[row+1][column+1] == "*":
			value += 1
		#south
		if real_board[row][column+1] == "*":
			value += 1
		#southwest
		if real_board[row-1][column+1] == "*":
			value += 1
		#west
		if real_board[row-1][column] == "*":
			value += 1
		#northwest
		if real_board[row-1][column-1] == "*":
			value += 1

	real_board[row][column] = str(value)

#################################################################################
#reveals all adjacent 0 on displayed_board
def display_adjacent_empty_squares(row, column):

	####################################################
	#left side boarder
	if row == 0:
		#top left corner
		if column == 0:
			#east
			if real_board[row+1][column] == "0":
				displayed_board[row+1][column] = real_board[row+1][column]
			#southeast
			if real_board[row+1][column+1] == "0":
				displayed_board[row+1][column+1] = real_board[row+1][column+1]
			#south
			if real_board[row][column+1] == "0":
				displayed_board[row][column+1] = real_board[row][column+1]

		#bottom left corner
		elif column == 8:
			#east
			if real_board[row+1][column] == "0":
				displayed_board[row+1][column] = real_board[row+1][column]
			#northeast
			if real_board[row+1][column-1] == "0":
				displayed_board[row+1][column-1] = real_board[row+1][column-1]
			#north
			if real_board[row][column-1] == "0":
				displayed_board[row][column-1] = real_board[row][column-1]

		#not corner left side
		else:
			#north
			if real_board[row][column-1] == "0":
				displayed_board[row][column-1] = real_board[row][column-1]
			#northeast
			if real_board[row+1][column-1] == "0":
				displayed_board[row+1][column-1] = real_board[row+1][column-1]
			#east
			if real_board[row+1][column] == "0":
				displayed_board[row+1][column] = real_board[row+1][column]
			#southeast
			if real_board[row+1][column+1] == "0":
				displayed_board[row+1][column+1] = real_board[row+1][column+1]
			#south
			if real_board[row][column+1] == "0":
				displayed_board[row][column+1] = real_board[row][column+1]

	####################################################
	#right side boarder
	elif row == 8:
		#top right corner
		if column == 0:
			#west
			if real_board[row-1][column] == "0":
				displayed_board[row-1][column] = real_board[row-1][column]
			#southwest
			if real_board[row-1][column+1] == "0":
				displayed_board[row-1][column+1] = real_board[row-1][column+1]
			#south
			if real_board[row][column+1] == "0":
				displayed_board[row][column+1] = real_board[row][column+1]

		#bottom right corner
		elif column == 8:
			#west
			if real_board[row-1][column] == "0":
				displayed_board[row-1][column] = real_board[row-1][column]
			#northwest
			if real_board[row-1][column-1] == "0":
				displayed_board[row-1][column-1] = real_board[row-1][column-1]
			#north
			if real_board[row][column-1] == "0":
				displayed_board[row][column-1] = real_board[row][column-1]

		#not corner right side
		else:
			#north
			if real_board[row][column-1] == "0":
				displayed_board[row][column-1] = real_board[row][column-1]
			#northwest
			if real_board[row-1][column-1] == "0":
				displayed_board[row-1][column-1] = real_board[row-1][column-1]
			#west
			if real_board[row-1][column] == "0":
				displayed_board[row-1][column] = real_board[row-1][column]
			#southwest
			if real_board[row-1][column+1] == "0":
				displayed_board[row-1][column+1] = real_board[row-1][column+1]
			#south
			if real_board[row][column+1] == "0":
				displayed_board[row][column+1] = real_board[row][column+1]

	####################################################
	#top side boarder
	elif column == 0:
		#east
		if real_board[row+1][column] == "0":
			displayed_board[row+1][column] = real_board[row+1][column]
		#southeast
		if real_board[row+1][column+1] == "0":
			displayed_board[row+1][column+1] = real_board[row+1][column+1]
		#south
		if real_board[row][column+1] == "0":
			displayed_board[row][column+1] = real_board[row][column+1]
		#southwest
		if real_board[row-1][column+1] == "0":
			displayed_board[row-1][column+1] = real_board[row-1][column+1]
		#west
		if real_board[row-1][column] == "0":
			displayed_board[row-1][column] = real_board[row-1][column]


	####################################################
	#bottom side boarder
	elif column == 8:
		#east
		if real_board[row+1][column] == "0":
			displayed_board[row+1][column] = real_board[row+1][column]
		#northeast
		if real_board[row+1][column-1] == "0":
			displayed_board[row+1][column-1] = real_board[row+1][column-1]
		#north
		if real_board[row][column-1] == "0":
			displayed_board[row][column-1] = real_board[row][column-1]
		#northwest
		if real_board[row-1][column-1] == "0":
			displayed_board[row-1][column-1] = real_board[row-1][column-1]
		#west
		if real_board[row-1][column] == "0":
			displayed_board[row-1][column] = real_board[row-1][column]


	####################################################
	#not outer edge (perimeter) of the board
	else:
		#north
		if real_board[row][column-1] == "0":
			displayed_board[row][column-1] = real_board[row][column-1]
		#northeast
		if real_board[row+1][column-1] == "0":
			displayed_board[row+1][column-1] = real_board[row+1][column-1]
		#east
		if real_board[row+1][column] == "0":
			displayed_board[row+1][column] = real_board[row+1][column]
		#southeast
		if real_board[row+1][column+1] == "0":
			displayed_board[row+1][column+1] = real_board[row+1][column+1]
		#south
		if real_board[row][column+1] == "0":
			displayed_board[row][column+1] = real_board[row][column+1]
		#southwest
		if real_board[row-1][column+1] == "0":
			displayed_board[row-1][column+1] = real_board[row-1][column+1]
		#west
		if real_board[row-1][column] == "0":
			displayed_board[row-1][column] = real_board[row-1][column]
		#northwest
		if real_board[row-1][column-1] == "0":
			displayed_board[row-1][column-1] = real_board[row-1][column-1]


###########################################################################
#places ten mines on real_board
def set_mines():
	i = 0
	while i < mines:
		row = random.randint(0,8)
		column = random.randint(0,8)
		if real_board[row][column] == "*":
			i += 0
		else:
			real_board[row][column] = "*"
			i += 1

###########################################################################
#puts adjacent mine numbers on the real_board
def solve_real_board():
	for i in range(len(real_board)):
		for j in range(len(real_board[i])):
			if not real_board[i][j] == "*":
				count_adjacent_mines(i, j)


###########################################################################
#shows player board
def print_displayed_board():
	print("  1 2 3 4 5 6 7 8 9")
	for i in range(len(displayed_board)):
		print(i+1, " ".join(displayed_board[i]))


###########################################################################
#shows the real_board with mines
def print_real_board():
	print("  1 2 3 4 5 6 7 8 9")
	for i in range(len(real_board)):
		print(i+1, " ".join(real_board[i]))


def play_again():
	displayed_board = [["-" for i in range(9)] for j in range(9)]
	real_board = [["-" for i in range(9)] for j in range(9)]
	set_mines()
	print_displayed_board()
	solve_real_board()


###########################################################################
def main():
	global displayed_board, real_board, running
	set_mines()
	print("Minesweeper: (press \"q\" to quit and \"cheat\" to cheat)\n")
	print_displayed_board()
	solve_real_board()
	while running:
		row = input("Input row(across): ")
		column = input("Input column(down): ")

		#quit if input contains q
		if "q" in row or "q" in column:
			break

		#shows solution if input contains cheat
		if "cheat" in row or "cheat" in column:
			print_real_board()
			print("CHEAT USED")
			continue

		#prints error if invalid input
		try:
			displayed_board[int(row)-1][int(column)-1] = real_board[int(row)-1][int(column)-1]
		except:
			print("Error with inputs, try again")
			continue

		#hits mine ends game
		if displayed_board[int(row)-1][int(column)-1] == "*":
			print_displayed_board()
			print("GAME OVER! YOU HIT A BOMB!")
			break

		display_adjacent_empty_squares(int(row)-1, int(column)-1)

		#checks nearby empty squares
		for i in range(len(displayed_board)):
			for j in range(len(displayed_board[i])):
				if displayed_board[j][i] == "0":
					display_adjacent_empty_squares(j,i)


		displayed_squares = 0

		#win
		for i in range(len(displayed_board)):
			for j in range(len(displayed_board[i])):
				if not displayed_board[i][j] == "-":
					displayed_squares += 1

		if displayed_squares == (board_width*board_height - mines):
			print("YOU WIN!!!!")
			break
		
		print_displayed_board()



if __name__ == '__main__':
	main()