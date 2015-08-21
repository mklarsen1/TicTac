from os import system, popen
from time import sleep
from random import randint

class gamesquares():
	def __init__(self, sq1 = " ", sq2 = " ", sq3 = " ", sq4 = " ", sq5 = " ", sq6 = " ", sq7 = " ", sq8 = " ", sq9 = " "):
		self.sq1 = sq1
		self.sq2 = sq2
		self.sq3 = sq3
		self.sq4 = sq4
		self.sq5 = sq5
		self.sq6 = sq6
		self.sq7 = sq7
		self.sq8 = sq8
		self.sq9 = sq9

	def testprintsquares(self):
		print self.sq1, self.sq2, self.sq3, "\n",\
self.sq4, self.sq5, self.sq6, "\n",\
self.sq7, self.sq8, self.sq9

	def setsquare(self, square, charval):
		pc = printChars()
		xovalue = ""

		if charval == "X" or charval == "x": 
			xovalue = pc.xlist
		elif charval == "O" or charval == "o":
			xovalue = pc.olist
		elif charval == " ":
			xovalue = pc.blank
		elif charval == "T" or charval == "t":
			xovalue = pc.t
		elif charval == "I" or charval == "i":
			xovalue = pc.i
		elif charval == "C" or charval == "c":
			xovalue = pc.c
		elif charval == "A" or charval == "a":
			xovalue = pc.a
		elif charval == "E" or charval == "e":
			xovalue = pc.e

		if square == 1: self.sq1 = xovalue
		elif square == 2: self.sq2 = xovalue
		elif square == 3: self.sq3 = xovalue
		elif square == 4: self.sq4 = xovalue
		elif square == 5: self.sq5 = xovalue
		elif square == 6: self.sq6 = xovalue
		elif square == 7: self.sq7 = xovalue
		elif square == 8: self.sq8 = xovalue
		elif square == 9: self.sq9 = xovalue
	
	def getsquares(self):
		allsquares = (self.sq1, self.sq2, self.sq3, self.sq4, self.sq5, self.sq6, self.sq7, self.sq8, self.sq9)
		return allsquares

class printChars():
	def __init__(self): 
		self.xlist = ("XX        XX",\
		"  XX    XX  ",\
		"    XX XX   ",\
		"      X     ",\
		"    XX XX   ",\
		"  XX    XX  ",\
		"XX        XX")

		self.olist = ("    OOOO    ",\
		"  OOOOOOOO  ",\
		" OOO    OOO ",\
		" OO      OO ",\
		" OOO    OOO ",\
		"  OOOOOOOO  ",\
		"    OOOO    ")

		self.vline = ("|", "|", "|", "|", "|", "|", "|")

		self.blank = ("            ",\
		"            ",\
		"            ",\
		"            ",\
		"            ",\
		"            ",\
		"            ")


		self.t = (" TTTTTTTTTT ",\
		" TTTTTTTTTT ",\
		"     TTT    ",\
		"     TTT    ",\
		"     TTT    ",\
		"     TTT    ",\
		"     TTT    ")


		self.i = ("  IIIIIIII  ",\
		"     III    ",\
		"     III    ",\
		"     III    ",\
		"     III    ",\
		"     III    ",\
		"  IIIIIIIII ")

		self.c = ("    CCCCC    ",\
		"  CCC   CCC  ",\
		" CC       CC ",\
		" CC          ",\
		" CC       CC ",\
		"  CCC   CCC  ",\
		"    CCCCC    ")

		self.a = ("      A     ",\
		"     A A    ",\
		"    A   A   ",\
		"   A     A  ",\
		"  AAAAAAAAA ",\
		" AA       AA",\
		" AA       AA")


		self.e = (" EEEEEEEEEE ",\
		" EEE        ",\
		" EEE        ",\
		" EEEEEEE    ",\
		" EEE        ",\
		" EEE        ",\
		" EEEEEEEEEE ")

		self.hline = "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"

		self.gamegrid = ("HHHHHHHHHHH", "H         H", "H  1 2 3  H", "H  4 5 6  H", "H  7 8 9  H", "H         H", "HHHHHHHHHHH")

	def printz(self):
		pass

	def printline1(self, list1, list2, list3):
		print "\n"
		cc = centerclass()
		for i in range(len(self.xlist)):
			m = list1[i], self.vline[i], list2[i], self.vline[i], list3[i] 
			n = "".join(m)
			cc.cr(n)

	def printline2(self, list1, list2, list3):
		cc = centerclass()
		for i in range(len(self.xlist)):
			m = list1[i], self.vline[i], list2[i], self.vline[i], list3[i]
			n = "".join(m)
			cc.cr(n)


	def printline3(self, list1, list2, list3):
		cc = centerclass()
		for i in range(len(self.xlist)):
			m = list1[i], self.vline[i], list2[i], self.vline[i], list3[i] 
			n = "".join(m)
			cc.cr(n)
		print "\n"

	def printguide(self):
		cc = centerclass()
		for i in range(len(self.gamegrid)):
			cc.cr(self.gamegrid[i])
			

	def printhline(self):
		cc = centerclass()
		cc.cr(self.hline)

	def printboard(self, *args):
		self.board = list(args)
		self.printline1(self.board[0][0], self.board[0][1], self.board[0][2])
		self.printhline()
		self.printline2(self.board[0][3], self.board[0][4], self.board[0][5])
		self.printhline()
		self.printline3(self.board[0][6], self.board[0][7], self.board[0][8])

	def printboardslow(self, *args):
		self.board = list(args)
		sleep(0.1)
		self.printline1(self.board[0][0], self.board[0][1], self.board[0][2])
		sleep(0.1)
		self.printhline()
		self.printline2(self.board[0][3], self.board[0][4], self.board[0][5])
		sleep(0.1)
		self.printhline()
		self.printline3(self.board[0][6], self.board[0][7], self.board[0][8])

class boardloop():
	def __init__(self, loopnumber, timeToSleep):
		self.timesleep = timeToSleep
		self.loopnumber = loopnumber
		pc = printChars()
		g = gamesquares()

		for i in range(0,self.loopnumber+1):
			system('clear')
			for i in range(0,10):
				g.setsquare(i,"X")
			board = g.getsquares()
			pc.printboard(board)
			sleep(self.timesleep)

			pc.printboard(board)
			system('clear')

			g.setsquare(2,"O")
			g.setsquare(4,"O")
			g.setsquare(6,"O")
			g.setsquare(8,"O")

			board = g.getsquares()
			pc.printboard(board)
			sleep(self.timesleep)
			system('clear')
			g.setsquare(5,"O")
			board = g.getsquares()
			pc.printboard(board)

			g.setsquare(1,"O")
			g.setsquare(9,"O")
			sleep(self.timesleep)
			system('clear')
			g.setsquare(5,"O")
			board = g.getsquares()
			pc.printboard(board)

			g.setsquare(3,"O")
			g.setsquare(7,"O")
			sleep(self.timesleep)
			system('clear')
			g.setsquare(5,"O")
			board = g.getsquares()
			pc.printboard(board)

	def tictactoe(self):
		system('clear')
		pc = printChars()
		g = gamesquares()
		for i in range(0,10):
			g.setsquare(i," ")
		g.setsquare(1, "T")
		g.setsquare(2, "I")
		g.setsquare(3, "C")
		g.setsquare(4, "T")
		g.setsquare(5, "A")
		g.setsquare(6, "C")
		g.setsquare(7, "T")
		g.setsquare(8, "O")
		g.setsquare(9, "E")
		board = g.getsquares()
		pc.printboardslow(board)
		sleep(1)

class centerclass():
	def __init__(self):
		self.rows, self.columns = popen('stty size', 'r').read().split()

	def cr(self, inputstring):
		print " " * ((int(self.columns)/2 - len(inputstring)/2) - 1), inputstring

class gamevalues():
	def __init__(self):
		self.whostarts = ""
		self.sq1 = ""
		self.sq2 = ""
		self.sq3 = ""
		self.sq4 = ""
		self.sq5 = ""
		self.sq6 = ""
		self.sq7 = ""
		self.sq8 = ""
		self.sq9 = ""
		self.userin = ""

	def getUserInput(self, numbersquare, starter, tempboard):
		if numbersquare == 0:
			self.userin = raw_input("Enter a square for " + starter + " (r for random): ")
			if self.userin == "r" or self.userin == "R":
				randomgeneratednumber = randint(1,9)
				while tempboard[randomgeneratednumber] == "X" or tempboard[randomgeneratednumber] == "O":
					randomgeneratednumber = randint(1,9)
				numbersquare = randomgeneratednumber 
				return numbersquare
			try: 
				self.userin = int(self.userin)
			except: 
				print "Not a number."
				sleep(1)
				numbersquare = self.getUserInput(numbersquare, starter, tempboard)
				return numbersquare
			if self.userin >= 10:
				print "Too high."
				sleep(1)
				numbersquare = self.getUserInput(numbersquare, starter, tempboard)
				return numbersquare
			elif self.userin < 0:
				print "Too low."
				sleep(1)
				numbersquare = self.getUserInput(numbersquare, starter, tempboard)
				return numbersquare
			else:
				numbersquare = self.userin
				return numbersquare
		else:
			return numbersquare

	def winner(self, board):
		pc = printChars()
		tempboard = list()
		tempboard.append(" ")
		for i in board:
			if i == pc.xlist: tempboard.append("X")
			elif i == pc.olist: tempboard.append("O")
			elif i == pc.blank: tempboard.append(" ")
		sleep(0.1)
		winningconditions = list()
		# row 1
		if tempboard[1] == "X" and tempboard[2] == "X" and tempboard[3] == "X": return True
		elif tempboard[1] == "O" and tempboard[2] == "O" and tempboard[3] == "O": return True
		# row 2
		elif tempboard[4] == "X" and tempboard[5] == "X" and tempboard[6] == "X": return True
		elif tempboard[4] == "O" and tempboard[5] == "O" and tempboard[6] == "O": return True
		# row 3
		elif tempboard[7] == "X" and tempboard[8] == "X" and tempboard[9] == "X": return True
		elif tempboard[7] == "O" and tempboard[8] == "O" and tempboard[9] == "O": return True
		# column 1
		elif tempboard[1] == "X" and tempboard[4] == "X" and tempboard[7] == "X": return True
		elif tempboard[0] == "O" and tempboard[4] == "O" and tempboard[7] == "O": return True
		# column 2
		elif tempboard[2] == "X" and tempboard[5] == "X" and tempboard[8] == "X": return True
		elif tempboard[2] == "O" and tempboard[5] == "O" and tempboard[8] == "O": return True
		# column 3
		elif tempboard[3] == "X" and tempboard[6] == "X" and tempboard[9] == "X": return True
		elif tempboard[3] == "O" and tempboard[6] == "O" and tempboard[9] == "O": return True
		# cross 1
		elif tempboard[1] == "X" and tempboard[5] == "X" and tempboard[9] == "X": return True
		elif tempboard[1] == "O" and tempboard[5] == "O" and tempboard[9] == "O": return True
		# cross 2
		elif tempboard[3] == "X" and tempboard[5] == "X" and tempboard[7] == "X": return True
		elif tempboard[3] == "O" and tempboard[5] == "O" and tempboard[7] == "O": return True
		else: return False


	def playstart(self, whostarts):
		system('clear')
		self.whostarts = whostarts
		g = gamesquares()
		pc = printChars()
		for i in range(0,10):
			g.setsquare(i," ")
		board = g.getsquares()

		if whostarts == "x" or whostarts == "X":
			starter = "X"
		elif whostarts == "o" or whostarts == "O":
			starter = "O"

		system('clear')

		for i in range(1,10):
			system('clear')
			pc.printboard(board)
			pc.printguide()

			tempboard = list()
			tempboard.append(" ")
			for i in board:
				if i == pc.xlist: tempboard.append("X")
				elif i == pc.olist: tempboard.append("O")
				elif i == pc.blank: tempboard.append(" ")

			self.userin = self.getUserInput(0, starter, tempboard)
			try:
				while tempboard[self.userin] == "X" or tempboard[self.userin] == "O":
					print "That square is occupied. Try again."
					self.userin = self.getUserInput(0, starter, tempboard)
			except:
				print "No input detected. Exiting."
				exit(1)
			g.setsquare(self.userin,starter)
			board = g.getsquares()
#			CHECK FOR WINNER
			whichwinner = ""
			if self.winner(board):
				system('clear')
				pc.printboard(board)
				break

			if starter == "X": 
				starter = "O"
			else: starter = "X"

		system('clear')
		pc.printboard(board)
		cc = centerclass()
		if self.winner(board):
			cc.cr(starter + " is the winner!")
		else:
			cc.cr("It's a draw!")		

bl = boardloop(2, 0.1)
bl.tictactoe()
g = gamevalues()
g.playstart("X")
