'''
Rock, Paper, Scissors
Version 1.9
Created By Austin G. Imperial
Created with Sublime Text
'''
from random import randint
def RPS():
	print ""
	print "ROCK, PAPER, SCISSORS V1.9"
	print ""
	print "Welcome, LET'S PLAY!!!"
	print "Best of 3 rounds!"
	print "May the best MAN/COMPUTER WIN!!!"
	print ""
	for round in range(1,4):
		if round == 1:
			pscore = 0
			ascore = 0
		print "Round" , round
		player = raw_input("Choose: rock, paper or scissors? ").upper()
		rand = randint(1,3)
		if rand == 1:
			rand = "ROCK"
		elif rand == 2:
			rand = "PAPER"
		else:
			rand = "SCISSORS"
		ai = rand
	
		# CHECKING
		if player == ai:
			rwin = "NO ONE"
		elif player == "ROCK":
			if ai == "SCISSORS":
				rwin = "YOU"
			else:
				rwin = "AI"
		elif player == "PAPER":
			if ai == "ROCK":
				rwin = "YOU"
			else:
				rwin = "AI"
		elif player == "SCISSORS":
			if ai == "PAPER":
				rwin = "YOU"
			else:
				rwin = "AI"
	
		if rwin == "YOU":
			pscore += 1
		elif rwin == "AI":
			ascore += 1
		print "YOUR choice is "+player+", and the AI's choice is "+ai+" so that means "+rwin+" WON this round!"
		print "SCORE: "+str(pscore)+"-"+str(ascore)
		print ""
	if pscore == ascore:
		print "And the winner is... NO ONE!!!"
	elif pscore > ascore:
		print "And the winner is... YOU!!!"
	else:
		print "And the winner is... AI!!!"
	print

	retry = raw_input("If you want to play again type (P)lay again but if you don't want to play anymore (because you lost) just click the [ X ] button on the upper right corner of your screen. (dumbass...): ").upper
	if retry == "P" or "PLAY AGAIN":
		RPS()
play = raw_input("Type (P)lay to Begin: ").upper
if play == "P" or "PLAY":
	RPS()