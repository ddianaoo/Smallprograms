def print_matrix(matrix, n, width=1): #функцию print_matrix() для вывода квадратной матрицы размерности n
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
