#!/usr/bin/env python3

import operator
from collections.abc import Iterable
from typing import Callable

from puzzle_input_getter import get_puzzle_input

MODULUS: int = 100


def get_direction_turns(line: str) -> tuple[Callable[[int, int], int], int]:
    direction = operator.add if line[0] == "R" else operator.sub
    turns = int(line[1:])
    return direction, turns


def part1(lines: Iterable[str]) -> int:
    zeros: int = 0
    pos: int = 50
    for line in lines:
        direction, turns = get_direction_turns(line)
        pos = direction(pos, turns) % MODULUS
        if pos == 0:
            zeros += 1
    return zeros


def part2(lines: Iterable[str]) -> int:
    zeros: int = 0
    pos: int = 50
    for line in lines:
        direction, turns = get_direction_turns(line)

        npos = direction(pos, turns)
        if npos == 0:
            zeros += 1

        n, npos = divmod(npos, MODULUS)

        zeros += abs(n)

        # special case rotating left
        if n < 0:
            if pos == 0 and npos != 0:
                zeros -= 1
            if npos == 0:
                zeros += 1

        pos = npos

    return zeros


if __name__ == "__main__":
    lines = get_puzzle_input(2025, 1).splitlines()
    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")
