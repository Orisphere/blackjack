import random

class Deck:
	
	def __init__(self, decks):
		deck = self.generate_deck()
		self.cards = []
		for i in range(decks):
			self.cards = self.cards + deck	
		self.shuffle()

	def generate_deck(self):
		suits = ["spades", "diamonds", "hearts", "clubs"]
		numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
		deck = []

		for s in suits: 
			for n in numbers:
				deck.append((n,s))
		return deck
	
	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		if self.cards is []:
			return None
		else:
			card = self.cards.pop()
			return card
	
class Blackjack:
	
	def __init__(self, players):
		self.players = players 
		self.cards = Deck(8)
		self.hand =[]
		
	def deal(self):
		for i in range(2):
			for p in self.players:
				p.hand.append(self.deck.deal())	
			if i == 0:
				self.hand.append(self.deck.deal())
		
	
	def bet(players):
		return None
		
	def get_points(hand):
		return 0

	
	def hit(player):
		

	def split(player):
		return None

	def double(player):
		return None

	def surrender(player):
		return None

	def stand(player):
		return None
	
	def make_move(player):
		finished = False
		
		while not finished:
			move = player.move()
			if move == 'hit':
				hit(p)
				if get_points(p.hand) > 21:
					finished = True
			if move == 'stand':
				stand(p)
				finished = True
			if move == 'surrender':
				surrender(p)
				finished = True
			if move == 'double':
				double(p)
				finished = True
			if move == 'split':
				split(p)


	def play_game(self):
		self.bet()
		self.deal()
		
		for p in self.players:
			make_move(p)
		
		self.hand.append(self.deck.deal())

		while get_points(self.hand) < 17:
			self.hand.append(self.deck.deal()) 

		if get_points(self.hand) > 21:
			#do something
		


		
class Player:

	def __init__(self,money):
		self.money = money
		self.hand = []

	def bet(self, x):
		return None
	
	def move(self):
		#assess hand pick move
		return None
c = Blackjack(['bob'])
