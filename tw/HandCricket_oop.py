class Player():
	def __init__(self,name):
		self.name = name
		self.score = 0

class Match():
	def __init__(self):
		self.winner = -1

	def round_match(self,A,B,batting): 	
		a = input("A throws?")
		b = input("B throws?")
		valid_score = [0,1,2,3,4,6]
		if a not in valid_score:
			print "A , dont be naughty. Throw a valid move"
			a = input("A throws?")
		if b not in valid_score:
			print "B , dont be naughty. Throw a valid move"
			b = input("B throws?")

		count = 0
		while(a!=b):
			if batting == "A":
				A.score += a
			else:
				B.score += b
			count += 1
			if count == 6:
				print "Its an over"
				break 
			a = input("A throws?")
			b = input("B throws?")
			if a not in valid_score:
				print "A , dont be naughty. Throw a valid move"
			if b not in valid_score:
				print "B , dont be naughty. Throw a valid move"


		print "%s is out"%batting
		if batting == "A": # repetative
			print "Score is %s"%A.score
		else:
			print "Score is %s"%B.score
	def play(self):
		player_a = Player("A")
		player_b = Player("B")

		batfirst = input("Who bats first?")
		print "Round 1 : %s is batting"%batfirst
		self.round_match(player_a,player_b,batfirst)

		batnext = "B" if batfirst == "A" else "A"
		print "Round 2 : %s is batting"%batnext
		self.round_match(player_a,player_b,batnext)

		print "A Scored:%s B Scored %s"%(player_a.score, player_b.score)
		if (player_a.score > player_b.score):
			print "Player A has won the game"
			self.winner = 0
		elif(player_a.score < player_b.score):
			print "Player B has won the game"
			self.winner = 1
		else:
			print "Its a tie"
			self.winner = -1
	


class Tournament():
	def start(self):
		Matches = 5
		winner_a = 0
		winner_b = 0
		for i in range(Matches):
			print "Match %s"%(i+1)
			match = Match()
			match.play()

			print match.winner
			if match.winner == 0:
				winner_a += 1
			elif match.winner == 1:
				winner_b +=1

		print winner_a,winner_b
		if winner_a > winner_b:
			print "A has won the Tournament"
		elif winner_b > winner_a:
			print "B has won the Tournament"
		else:
			print "Its a Tie"


if __name__ == "__main__":
	t = Tournament()
	t.start()

	