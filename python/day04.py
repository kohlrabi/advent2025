#!/usr/bin/env python3

from collections.abc import Iterable

import numpy as np
import scipy.signal

from puzzle_input_getter import get_puzzle_input


def part1(lines) -> int:
    kernel = np.ones((3, 3), dtype="uint")
    kernel[1, 1] = 0

    conv = scipy.signal.convolve2d(lines, kernel, mode="same")

    return (conv[lines] < 4).sum()


def part2(lines: Iterable[str]) -> int:
    return 0


if __name__ == "__main__":
    lines = get_puzzle_input(2025, 4).splitlines()

    lines = np.array([[False if x == "." else True for x in line] for line in lines], dtype=bool)

    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")
