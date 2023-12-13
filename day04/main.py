"""
Advent of Code
Day 4 - Scratchcards
"""
from pathlib import Path


class Card:

    def __init__(
        self,
        number: int,
        test_numbers: list[int],
        winning_numbers: list[int],
        copies: int = 1
    ) -> None:
        self.number = number
        self.test_numbers = test_numbers
        self.winning_numbers = winning_numbers
        self.copies = copies

    @property
    def matches(self) -> list[int]:
        return [x for x in self.test_numbers if x in self.winning_numbers]

    @property
    def num_matches(self) -> int:
        return len(self.matches)


def clean_line(line: str) -> list[str]:
    """Split a card into winning numbers and 'your' numbers."""
    nums = line.split(':')[1]
    return nums.split('|')


def str_to_list(int_str: str, delim: str = ' ') -> list[int]:
    """Convert a list of strings to integers."""
    return [int(x) for x in int_str.split(delim) if x != '']


def solve_1(text: list[str]) -> int:
    """
    Solution to Part 1.
    """
    ttl_points = 0

    for line in text:
        my_nums, winning_nums = clean_line(line)

        my_nums = str_to_list(my_nums)
        winning_nums = str_to_list(winning_nums)

        matches = [x for x in my_nums if x in winning_nums]

        card_points = 0 if not matches else 2 ** (len(matches) - 1)

        ttl_points += card_points

    return ttl_points


def solve_2(text: list[str]) -> int:
    """
    Solution to Part 2.
    """
    ttl_points = 0
    card_idx = 1
    cards = {}

    for line in text:
        my_nums, winning_nums = clean_line(line)
        cards[card_idx] = Card(card_idx, my_nums, winning_nums)
        card_idx += 1

    for key, val in cards.items():
        if val.num_matches != 0:
            for x in range(val.num_matches + 1):
                try:
                    cards[key + x].copies += 1
                except KeyError:
                    cards[key].copies += 1

    num_cards = 1
    for key, val in cards.items():
        num_cards *= val.copies

    return num_cards


if __name__ == '__main__':
    raw_cards = Path(__file__).with_name('input.txt').read_text().readlines()

    cards = [x.strip() for x in raw_cards]

    #soln = solve_1(test_input)
    soln = solve_2(test_input)

    print(soln)
