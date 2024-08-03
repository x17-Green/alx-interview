#!/usr/bin/python3
"""Method that determines if all the boxes can be opened.

Args:
    boxes (list): A list of lists, where each inner list
    represents a box and its contents are the keys to other boxes.

Returns:
    bool: True if all boxes can be opened, False otherwise.

Example:
    >>> canUnlockAll([[1], [2], [3], [4]])
    True
    >>> canUnlockAll([[1, 4], [2], [3], [4]])
    False
    >>> canUnlockAll([[1, 3], [2], [0, 4], [4]])
    True
    >>> canUnlockAll([[]])
    False
    >>> canUnlockAll([])
    False

"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    The function takes a list of boxes as input,
    where each box is a list of keys to other boxes.

    It returns True if all boxes can be opened,
    False otherwise.
    """
    if (type(boxes) is not list):
        return False

    if len(boxes) == 0:
        return False

    keys = [0]
    for i in keys:
        for k in boxes[i]:
            if k not in keys and k != i and k < len(boxes) and k != 0:
                keys.append(k)
    if len(keys) == len(boxes):
        return True
    else:
        return False
