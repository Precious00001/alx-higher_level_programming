#!/usr/bin/python3
"""This function defines a Pascal's Triangle generator."""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for o in range(len(tri) - 1):
            tmp.append(tri[o] + tri[o + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
