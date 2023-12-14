"""
Advent of Code 2023
Day 14 - Parabolic Reflector Dish
"""
from pathlib import Path


SAMPLE_GRID = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....',
]


def pretty_print(grid: list[list[str]]) -> None:
    _ = [print(''.join(x)) for x in grid]


def explode(grid: list[str]) -> list[list[str]]:
    return [list(x) for x in grid]


def solve_1(grid: list[list[str]]) -> list[list[str]]:
    """Solution to Part 1."""

    def can_move(grid: list[list[str]], pos: tuple[int]) -> bool:
        """Can the stone move?"""
        val = False
        i, j = pos

        try:
            val = grid[i - 1][j] == '.'
        except IndexError:
            pass

        return val

    n_rows = len(grid)
    n_cols = len(grid[0])
    rounds = []

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 'O': rounds.append((i, j))

    for stone in rounds:
        curr_i, curr_j = i, j = stone

        while can_move(grid, (curr_i, curr_j)) and curr_i > 0:
            curr_i -= 1

        if (curr_i, curr_j) != (i, j):
            grid[curr_i][curr_j] = 'O'
            grid[i][j] = '.'

    sum = 0
    for i in range(n_rows):
        for j in range(n_cols):
            sum += n_rows - i if grid[i][j] == 'O' else 0

    return sum, grid


if __name__ == '__main__':
    #grid = explode(SAMPLE_GRID)
    grid = explode(Path(__file__).with_name('input.txt').read_text().splitlines())

    soln, grid = solve_1(grid)

    pretty_print(grid)
    print(soln)

