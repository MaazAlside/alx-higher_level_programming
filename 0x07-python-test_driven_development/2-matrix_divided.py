#!/usr/bin/python3

"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    args:
    matrix: list of lists of integers or floats
    div: a number (integer or float)
    """
    newMatrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for row in range(len(matrix)):
            first_row_size = len(matrix[0])
            newRow = []
            if len(matrix[row]) != first_row_size:
                raise TypeError("Each row of the matrix "
                                "must have the same size")
            for element in range(len(matrix[row])):
                if not isinstance(matrix[row][element], (int, float)):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
                else:
                    result = matrix[row][element] / div
                    newRow.append(round(result, 2))
            newMatrix.append(newRow)
    return newMatrix
