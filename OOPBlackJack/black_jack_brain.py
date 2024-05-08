class BlackJack:

    def __init__(self, take_card):
        self.take_card = take_card
        self.player_card = take_card.draw_start_card()
        self.computer_card = take_card.draw_start_card()

    def check_play(self):
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        return True if user_input == 'y' else False

    def display_card(self):
        print(f'\tYour cards: {self.player_card}, current score: {sum(self.player_card)}')
        print(f'\tComputer\' first card: {self.computer_card[0]}')

    def get_card(self, card):
        card + self.take_card.draw_one_card()

    def check_ace(self, card):
        if sum(card) > 21 and 11 in card:
            card[card.index[11]] = 1
