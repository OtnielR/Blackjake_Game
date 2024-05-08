from BlackJackArt import logo
from black_jack_brain import BlackJack
from draw_a_card import TakeCard

black_jack = BlackJack(TakeCard())

def main():
    print(logo)
    if black_jack.check_play():
        while True:
            black_jack.check_ace(black_jack.player_card)
            black_jack.display_card()
            user_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_input == 'y':
                black_jack.get_card(black_jack.player_card)
            else:
                break


if __name__ == '__main__':
    main()
