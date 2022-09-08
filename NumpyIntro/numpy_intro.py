# acme-include
# numpy_intro.py
"""Python Essentials: Intro to NumPy.
Vin Howe
<Class>
<Date>
"""

# acme-include
import numpy as np


# acme-include
def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array([
        [3, -1, 4],
        [1, 5, -9],
    ])
    B = np.array([
        [2, 6, -5, 3],
        [5, -8, 9, 7],
        [9, -3, -2, -3],
    ])
    return A @ B


# acme-include
def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([
        [3, 1, 4],
        [1, 5, 9],
        [-5, 3, 1]
    ])
    return -(A @ A @ A) + 9*A**2 - 15*A


# acme-include
def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7, 7)))
    B = (-5 * A.copy()) -np.tril(np.ones((7, 7)))
    return (A@B@A).astype(np.int64)


# acme-include
def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A_copy = A.copy()
    A_copy[A_copy < 0] = 0
    return A_copy


# acme-include
def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I | 8 = 3 + 2 + 3
                                | A  0  0 | 8 = 3 + 5
                                | B  0  C | 8 = 3 + 2x3 + 3
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    # 3x3 + 2x3 + 3x3
    # 3x2 + 
    #
    A = np.array([
        [0, 2, 4],
        [1, 3, 5]
    ])
    B = np.tril(np.ones((3, 3)) * 3)
    C = np.diag(-2 * np.ones(3))
    top = np.hstack((np.zeros((3, 3)), A.T, np.diag(np.ones(3))))
    middle = np.hstack((A, np.zeros((2, 5))))
    bottom = np.hstack((B, np.zeros((3, 2)), C))
    return np.vstack((top, middle, bottom))


# acme-include
def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    return A / A.sum(axis=1, keepdims=True)


# acme-include
def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    grid = np.load('grid.npy')
    horizontal = np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    vertical = np.max(grid[:-3] * grid[1:-2] * grid[2:-1] * grid[3:])
    right_diagonal = np.max(grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:])
    left_diagonal = np.max(grid[:-3,3:] * grid[1:-2,2:-1] * grid[2:-1,1:-2] * grid[3:,:-3])
    return np.max([horizontal, vertical, right_diagonal, left_diagonal])
