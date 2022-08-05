#!/usr/bin/python3
""" Method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    if not boxes:
        return False

    boxLen = len(boxes)
    boxOpen = [0]
    for k in boxOpen:
        for box in boxes[k]:
            if box not in boxOpen and box < boxLen:
                boxOpen.append(box)

    if len(boxOpen) == boxLen:
        return True

    return False
