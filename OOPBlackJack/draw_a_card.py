import random


class TakeCard:

    def __init__(self):
        self.cards = [11] + [_ for _ in range(2, 9 + 1)] + [10 for _ in range(4)]

    def draw_start_card(self):
        return [random.choice(self.cards) for _ in range(2)]

    def draw_one_card(self):
        return [random.choice(self.cards)]
