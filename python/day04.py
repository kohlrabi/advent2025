#!/usr/bin/env python3

import numpy as np
import scipy.signal
from numpy.typing import NDArray

from puzzle_input_getter import get_puzzle_input


def part1(grid: NDArray[np.bool]) -> int:
    kernel = np.ones((3, 3), dtype=np.uint)
    kernel[1, 1] = 0

    conv = scipy.signal.convolve2d(grid, kernel, mode="same")

    rolls = np.where(conv < 4, grid, False)

    return rolls.sum()


def part2(grid: NDArray[np.bool]) -> int:
    kernel = np.ones((3, 3), dtype=np.uint)
    kernel[1, 1] = 0

    total = 0
    while True:
        conv = scipy.signal.convolve2d(grid, kernel, mode="same")
        rolls = np.where(conv < 4, grid, False)

        if rolls.sum() == 0:
            break

        total += rolls.sum()
        grid[rolls] = False

    return total


if __name__ == "__main__":
    lines = get_puzzle_input(2025, 4).splitlines()

    grid = np.array([[False if x == "." else True for x in line] for line in lines], dtype=np.bool)

    print(f"part1: {part1(grid)}")
    print(f"part2: {part2(grid)}")
