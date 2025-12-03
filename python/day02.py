#!/usr/bin/env python3

import itertools

from puzzle_input_getter import get_puzzle_input

MODULUS: int = 100


def part1(line: str) -> int:
    invalid: int = 0

    ranges = (range(int((v := tup.split("-"))[0]), int(v[1]) + 1) for tup in line.split(","))
    for num in itertools.chain(*ranges):
        snum = str(num)
        n = len(snum)
        if n % 2 == 0 and snum[: n // 2] == snum[n // 2 :]:
            invalid += num

    return invalid


def part2(lines: str) -> int:
    return 0


if __name__ == "__main__":
    lines = get_puzzle_input(2025, 2).splitlines()
    print(f"part1: {part1(lines[0])}")
    print(f"part2: {part2(lines[0])}")
