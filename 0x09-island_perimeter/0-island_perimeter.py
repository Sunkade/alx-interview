#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    d = 0
    for c in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (c <= 0 or grid[i - 1][j] == 0):
                    d += 1
                if (c >= len(grid) - 1 or grid[i + 1][j] == 0):
                    d += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    d += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    d += 1
    return d
