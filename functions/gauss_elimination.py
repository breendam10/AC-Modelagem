import numpy as np

def gauss_elimination(A, b):
    """
    Resolve o sistema linear Ax = b usando eliminação de Gauss.
    A: matriz dos coeficientes (lista de listas ou np.array)
    b: vetor dos termos independentes (lista ou np.array)
    Retorna: vetor solução x
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    # Eliminação
    for i in range(n):
        # Pivoteamento parcial
        max_row = np.argmax(abs(A[i:, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x.tolist()