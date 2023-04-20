#!/usr/bin/python3
"""Calculate how many square units of water will be retained after it rains"""


def rain(walls):
    """Return: Integer indicating total amount of rainwater retained"""
    if not walls or not isinstance(walls, list):
        return 0

    l, water = len(walls), 0
    left, right = [0] * l, [0] * l

    left[0], right[l - 1] = walls[0], walls[l - 1]

    i, j = 1, l - 2

    while True:
        if i >= l or j <= -1:
            break

        left[i] = max(left[i - 1], walls[i])
        right[j] = max(right[j + 1], walls[j])

        i += 1
        j -= 1

    for i in range(l):
        water += min(left[i], right[i]) - walls[i]

    return water
