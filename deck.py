import random
class Deck(object):
	def __init__(self):
		self.deck = Range(52)
		self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		
	def reset(self):
		self.deck = Range(52)
	
	def shuffle(self):
		random.shuffle(self.deck)