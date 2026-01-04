from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0
percent_win = 0
card_string = ""
no_winner = True
player_hand = 0

def print_menu():
	print("")
	print("1. Get another card")
	print("2. Hold hand")
	print("3. Print statistics")
	print("4. Exit")
	print("")

def deal_card():
	global player_hand
	card = rng.next_int(13) + 1
	if card == 1:
		card_string = "ACE"
	elif 2<= card <= 10:
		card_string = str(card)
	elif card == 11:
		card_string = "JACK"
		card = 10
	elif card == 12:
		card_string = "QUEEN"
		card = 10
	elif card == 13:
		card_string = "KING"
		card = 10

	player_hand += card
	print("Your card is a " + str(card_string) + "!")
	print("Your hand is: " + str(player_hand))

# loop through games and incrementing game_num
while game_continue:
	player_hand = 0
	# 1. increment and print game_num
	game_num += 1
	print("START GAME #" + str(game_num))
	# 2. deal first cards (for player and dealer
	deal_card()
	
	no_winner = True
	while no_winner:
		print_menu()
		op = int(input("Choose an option:"))
		print("")
		if op == 1:
			deal_card()
			if player_hand == 21:
				player_wins += 1
				no_winner = False
				print("BLACKJACK! You win!")
			elif player_hand > 21:
				dealer_wins += 1
				no_winner = False
				print("You exceeded 21! You lose.")
		elif op == 2:
			#deal to dealer
			#compare player and dealer values, determine winner
			dealer_hand = rng.next_int(11) + 16
			print("Dealer's hand: " + str(dealer_hand))
			print("Your hand is: " + str(player_hand))
			print("")
			if player_hand > dealer_hand:
				print("You win!")
				player_wins += 1
			elif dealer_hand > 21:
				print("You win!")
				player_wins += 1
			elif dealer_hand > player_hand:
				print("Dealer wins!")
				dealer_wins += 1
			else:
				print("It's a tie! No one wins!")
				tie_games += 1
			no_winner = False

		elif op == 3:
			print("Number of Player wins: " + str(player_wins))
			print("Number of Dealer wins: " + str(dealer_wins))
			print("Number of tie games: " + str(tie_games))
			print("Total # of games played is: " + str(game_num -1))
			percent_win = (player_wins * 100) / (game_num -1)
			percent_win = round(percent_win, 2)
			print("Percentage of Player wins: " + str(percent_win) + "%")
		elif op == 4:
			no_winner = False #get out of inner loop
			game_continue = False #get out of outer loop
		else:
			print("Invalid input!")
			print("Please enter an integer value between 1 and 4.")