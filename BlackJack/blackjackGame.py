from deck import *
class BlackJackGame:
    """BlackJack game class"""
    def __init__(self, num_players):
        # Ask each player for their name and store it in a list 
        self.num_players = num_players
        self.players = []
        for players in range(num_players):
            name = input("Enter the name for player number {} ".format(players + 1))
            self.players.append(name)
        # Create a deck of cards and shuffle it
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        max_hand_value = 0
        winner = None
        # For each player, play a hand. 
        for player in self.players:
            hand_value = self.play_hand(player)
            print("{}'s hand value: {}".format(player, hand_value))

        # After all players have played, print the winner
        if hand_value <= 21 and hand_value > max_hand_value:
            max_hand_value = hand_value
            winner = player
        if winner:
            print("Winner: {} with a hand value of {}".format(winner, max_hand_value))
        else:
            print("No winners")

    def play_hand(self, player):
        hand_value = 0
        print("{}'s turn:".format(player))
        # Give a card to the player
        while True:
            card = self.deck.get_card()
            print("Received card: {}".format(card))
            if card.rank in ['Jack', 'Queen', 'King']:
                hand_value += 10
            elif card.rank == 'Ace':
                if hand_value + 11 <= 21:
                    hand_value += 11
                else:
                    hand_value += 1
            else:
                hand_value += int(card.rank)
            # the value obtained is 21 or over
            if hand_value >= 21:
                break
            # If the player wants a new card, give them a card
            # End the hand once the player asks for no more cards or when adding the card ranks
            response = input("Do you want another card y or no: ")
            if response.lower() != 'y':
                break
        # Return the total value of the hand (addition of all card ranks. If value is over 21, return 0)
        return hand_value