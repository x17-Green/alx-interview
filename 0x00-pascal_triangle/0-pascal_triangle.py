#!/usr/bin/python3
"""
0-pascal_triangle.py
"""
def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists, where each sublist represents a row in the Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle