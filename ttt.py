class TicTacToe:
	def __init__(self, psym, csym): # player symbol and comp symbol taken as args
		self.board = [['*' for i in range(3)] for j in range(3)] 
		self.csym = csym
		self.moves = 0
		self.psym = psym
		self.eval ={psym:-10, csym:10, 'tie':0} #evaluation scores for diff results

	def showBoard(self): # display board on command line
		for i in range(3):
			for j in range(3):
				print(self.board[i][j], end = '\t')
			print()

	
	def updtBoard(self, i, j, sym): # make one move
		self.board[i][j] = sym
		self.moves += 1

	
	def checkWin(self, moves = False): #returns the winning symbol, else returns False
		if not moves: #minimax sends an additional moves argument
			moves = self.moves
		if moves < 5:
			return False
		for i in range(3): #check horizontal rows
			if (self.board[i][0] == self.board[i][1]) and (self.board[i][0] == self.board[i][2]) and self.board[i][0] != '*':
				return self.board[i][0]

		for i in range(3): # check columns
			if (self.board[0][i] == self.board[1][i]) and (self.board[0][i] == self.board[2][i]) and self.board[0][i] != '*':
				return self.board[0][i]

		if (self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]) and self.board[0][0] != '*': #principle diag
			return self.board[0][0]

		if (self.board[2][0] == self.board[1][1]) and (self.board[2][0] == self.board[0][2]) and self.board[2][0] != '*':#other diag
			return self.board[2][0]

		return False #when there is no winner

	def play(self): # called to play the full game
		c = ' '
		end = False
		if self.psym == 'O': # X always starts
			i, j = self.bestmove()
			self.updtBoard(i,j,self.csym)
		while True:
			self.showBoard()
			if self.moves == 9:
				end = True
				break
			check = False
			pi, pj = -1, -1
			while not check:
				pi = int(input('Enter row index '))
				pj = int(input('Enter column index '))
				if self.board[pi][pj] != '*':
					print('Select empty location')
				else:
					check = True
			self.updtBoard(pi,pj,self.psym)
			c = self.checkWin()
			if c:
				break
			if self.moves == 9:
				end = True
				break
			i, j = self.bestmove()
			self.updtBoard(i,j,self.csym)
			c = self.checkWin()
			if c:
				break
		
		print('\nFinalBoard:\n')
		self.showBoard()
		if end:
			print('Tie')
		elif c == self.psym:
			print('Congrats, you have won!')
		else:
			print('You lost to the AI')


	def bestmove(self): #returns co-ordinates of best move to be made by AI
		bestscore = -100
		move = {}
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == '*':
					self.board[i][j] = self.csym
					score = self.minimax(False, self.moves+1) # determine the score of making that move, next move made by minimizer
					self.board[i][j] = '*'
					if score > bestscore: #select the best score
						bestscore = score
						move['i'] = i
						move['j'] = j
		return (move['i'], move['j'])

	def minimax(self, isMaximizing, moves):
		
		c = self.checkWin(moves)
		#terminal node conditions
		if c:
			return self.eval[c]
		elif not c and moves >= 9:
			return self.eval['tie']

		if isMaximizing: #maximizer will pick move that gives that leads to max score assuming opp plays optimally
			maxscore = -100
			for i in range(3):
				for j in range(3):
					if self.board[i][j] == '*':
						self.board[i][j] = self.csym
						score = self.minimax(False, moves+1) #recursively call, but next move is for minimizer
						self.board[i][j] = '*'
						maxscore = max(score,maxscore)
			return maxscore

		else:  #minimizer picks the move that leads to min score ( estimate of human's move )
			minscore = 100
			for i in range(3):
				for j in range(3):
					if self.board[i][j] == '*':
						self.board[i][j] = self.psym
						score = self.minimax(True, moves+1) #recursively call, but next move is for maximizer
						self.board[i][j] = '*'
						minscore = min(score, minscore)
			return minscore

if __name__ == '__main__':
	ag = True
	while ag:
		psym = input('Enter your symbol of choice (X or O): ')
		csym = {'X':'O','O':'X'}[psym]
		game = TicTacToe(psym, csym)
		game.play()
		if input('Enter y to play again, else any key ').lower() != 'y':
			ag = False




	
