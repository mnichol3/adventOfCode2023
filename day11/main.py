"""
Advent of Code 2023
Day 11 - Cosmic Expansion
"""
from pathlib import Path


SAMPLE_INP = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]


SAMPLE_INP_EXP = [
    '....#........',
    '.........#...',
    '#............',
    '.............',
    '.............',
    '........#....',
    '.#...........',
    '............#',
    '.............',
    '.............',
    '.........#...',
    '#....#.......',
]


def pretty_print(grid: list[list[str]]) -> None:
    for x in grid:
        print(x)


def explode(grid: list[str]) -> list[list[str]]:
    return [list(x) for x in grid]


def solve_1(grid: list[list[str]]) -> int:
    """Solution to Part 1."""
    visited = []
    distances = []

    empty_rows = [idx for idx, row in enumerate(grid) if set(row) == {'.'}]
    empty_cols = [x for x in range(len(grid[0])) if set([y[x] for y in grid]) == {'.'}]

    coords = [(i, j) for i, row in enumerate(grid) for j, ele \
               in enumerate(row) if ele == '#']

    for idx, coord in enumerate(coords):
        i, j = coord

        i += len([x for x in empty_rows if x < i])
        j += len([y for y in empty_cols if y < j])

        coords[idx] = (i, j, idx + 1)

    for idx, origin in enumerate(coords):
        for dest in coords[idx:]:
            path = f'{origin[2]}-{dest[2]}'
            if path not in visited:
                delta_i = abs(dest[0] - origin[0])
                delta_j = abs(dest[1] - origin[1])

                dist = delta_i + delta_j

                distances.append(dist)
                visited.append(path)

    return sum(distances)


def solve_2(grid: list[list[str]]) -> int:
    """Solution to Part 2."""
    raise NotImplementedError


def test_1() -> None:
    soln = solve_1(explode(SAMPLE_INP))
    assert soln == 374, f'{soln} != 374'

    print('Test 1 OK')


if __name__ == '__main__':
    inp = explode(Path(__file__).with_name('input.txt').read_text().splitlines())

    #test_1()
    soln = solve_1(inp)

    print(soln)

