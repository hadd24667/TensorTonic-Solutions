import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    Arr = np.array(A)
    rows, cols = Arr.shape
    A_t = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            A_t[j, i] = Arr[i, j]        
    return A_t
