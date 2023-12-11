"""
Advent of Code 2023
Day 9 - Mirage Maintenance
"""
import sys
from pathlib import Path


def read_input(fname: str = 'input.txt') -> list[list[float]]:
    """
    Read input from a text file and return it as nested lists of ints.

    Parameters
    ----------
    fname: str, optional
        Name of the file to read.
        Default is 'input.txt'.

    Returns
    -------
    list of lists of ints.
    Ex:
        [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]

    Raises
    ------
    FileNotFoundError
    """
    input = Path(__file__).with_name(fname).read_text().splitlines()

    input = [[int(x) for x in y.split()] for y in input]

    return input


def solve_1(hist: list[float]) -> float:
    """
    Solution for Part 1.

    Parameters
    ----------
    hist: list of float

    Return
    ------
    float
    """
    diffs = [hist[-1]]

    iter_list = hist
    while True:
        curr_diffs = [iter_list[idx + 1] - val for idx, val in enumerate(iter_list[:-1])]

        diffs.append(curr_diffs[-1])

        if list(set(curr_diffs)) == [0]:
            break

        iter_list = curr_diffs

    return sum(diffs)


def solve_2(hist: list[float]) -> float:
    """
    Solution for Part 1.

    Parameters
    ----------
    hist: list of float

    Return
    ------
    float
    """
    raise NotImplementedError


if __name__ == '__main__':
    inp = read_input()

    #print(sum([solve_1(x) for x in inp]))
    print(sum([solve_2(x) for x in inp]))
