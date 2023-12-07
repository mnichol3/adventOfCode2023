"""
Advent of Code 2023
Day 7 - Camel Cards
"""
from __future__ import annotations
from collections import Counter
from random import shuffle

from tree_sort import BinarySearchTree


class Hand:
    """
    A single hand dealt in the game of Camel Cards.
    """

    CARD_VALUE = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1,
    }

    HAND_VALUE = {
        '5ofkind': 7,
        '4ofkind': 6,
        'full_house': 5,
        '3ofkind': 4,
        '2pair': 3,
        '1pair': 2,
        'high_card': 1,
    }


    def __init__(self, cards: str, bid: float) -> None:
        """Initialize a hand instance."""
        self.cards = list(cards)
        self.bid = int(bid)
        self.winnings = 0
        self.rank = 0
        self.card_values = [self.CARD_VALUE.get(x) for x in self.cards]
        self.best_hand = self.get_best_hand()
        self.hand_strength = self.HAND_VALUE.get(self.best_hand)

    def get_best_hand(self) -> str:
        """Determine the strength of the given hand."""
        card_counter = Counter(self.cards)

        counts = sorted(list(card_counter.values()))
        num_count = len(counts)

        best = ''

        if num_count == 1:
            best = '5ofkind'
        if num_count == 2:
            best = '4ofkind' if counts == [1, 4] else 'full_house'
        elif num_count == 3:
            best = '3ofkind' if counts == [1, 1, 3] else '2pair'
        elif num_count == 4:
            best = '1pair'
        else:
            best = 'high_card'

        return best

    def _check_type(self, other: Hand) -> bool:
        if not isinstance(other, Hand):
            raise TypeError(f'Expected type Hand, got {type(other)}')

    def __lt__(self, other: Hand) -> bool:
        self._check_type(other)
        if not self.hand_strength == other.hand_strength:
            return self.hand_strength < other.hand_strength
        else:
            for idx, val in enumerate(self.card_values):
                if val != other.card_values[idx]:
                    return val < other.card_values[idx]

    def __le__(self, other: Hand) -> bool:
      self._check_type(other)
      raise NotImplementedError

    def __eq__(self, other: Hand) -> bool:
        self._check_type(other)
        if not self.hand_strength == other.hand_strength:
            return False
        else:
            return self.card_values == other.card_values

    def __ne__(self, other: Hand) -> bool:
        self._check_type(other)
        raise NotImplementedError

    def __gt__(self, other: Hand) -> bool:
        self._check_type(other)
        if not self.hand_strength == other.hand_strength:
            return self.hand_strength > other.hand_strength
        else:
            for idx, val in enumerate(self.card_values):
                if val != other.card_values[idx]:
                    return val > other.card_values[idx]

    def __ge__(self, other: Hand) -> bool:
        self._check_type(other)
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Hand {''.join(self.cards)} - {self.best_hand}>"


class CamelCards:
    """
    A game of Camel Cards.
    """

    def __init__(self, hand_list: list[str]) -> None:
        """Initialize a CamelCards instance."""
        self.hands = self.get_hands(hand_list)
        self.num_hands = len(self.hands)

    def get_hands(self, hand_list: list[str]) -> list[Hand]:
        """Return the given card hands as Card objects."""
        hand_objs = []

        for x in hand_list:
            curr_hand = Hand(*x.split(' '))
            hand_objs.append(curr_hand)

        return hand_objs

    def bogo_sort(self) -> list[Hand]:
        """
        :D
        """
        while not is_sorted(self.hand_ranks):
            shuffle(self.hands)

        return self.hands

    def tree_sort(self):
        my_tree = BinarySearchTree()
        my_tree.load(self.hands)

        return my_tree.sort()

    @staticmethod
    def is_sorted(data) -> bool:
        return all(a <= b for a, b in zip(data, data[1:]))

    @property
    def hand_ranks(self) -> list[float]:
        return [x.rank for x in self.hands]


def read_input(path: str) -> list[str]:
    """Read puzzle input from file."""
    with open(path, 'r') as f_in:
        hands = f_in.readlines()

    return [x.strip() for x in hands]


def get_sample_input() -> list[str]:
    """Get provided sample input."""
    sample = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
    ]

    return sample


def solve(input: list[str]) -> float:
    my_game = CamelCards(input)
    sorted_hands = my_game.tree_sort()

    sum = 0
    for idx, hand in enumerate(sorted_hands):
        hand.rank = idx + 1
        hand.winnings = hand.bid * hand.rank
        sum += hand.winnings

    return sum


def test() -> bool:
    """Quick & dirty unit test"""
    hands = get_sample_input()
    sum = solve(hands)

    assert sum == 6440, f'{sum} != 6440'

    return True


def main() -> None:
    input_file = 'input.txt'
    hands = read_input(input_file)
    sum = solve(hands)
    print(sum)


if __name__ == '__main__':
    #test()
    main()

    # 253051174 is too high lol