from sys import argv
import deck
script,num_players = argv
def numCardsToDeal(num_players):
	if num_players > 10:
		sys.exit("Cannot play fish with more than 10 players");
	elif 5 <= num_players <=10:
		cardsToDeal = 5
	else:
		cardsToDeal = 7
	return cardsToDeal
	
def dealCards(num_players):
	cardsToDeal = numCardsToDeal(num_players)
	newDeck = deck.Deck();
	for players in range(0, num_players):
		print "Dealing Cards for %d player" %players
		

def main(num_players):
	num_players = int(num_players)
	dealCards(num_players)
	


	
	
# Main called.	
main(num_players)