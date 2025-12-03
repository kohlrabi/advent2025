#!/usr/bin/env python3

from collections.abc import Iterable

from puzzle_input_getter import get_puzzle_input

MODULUS: int = 100


def part1(lines: Iterable[str]) -> int:
    joltage = 0

    for line in lines:
        bank = [int(digit) for digit in line]
        for num in range(9, 0, -1):
            try:
                ind = bank.index(num)
            except ValueError:
                continue
            if ind >= len(bank) - 1:
                continue

            for num2 in range(9, 0, -1):
                if num2 in bank[ind + 1 :]:
                    joltage += int(num * 10 + num2)
                    break
            else:
                continue
            break

    return joltage


def part2(lines: Iterable[str]) -> int:
    return 0


if __name__ == "__main__":
    lines = get_puzzle_input(2025, 3).splitlines()
    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")
