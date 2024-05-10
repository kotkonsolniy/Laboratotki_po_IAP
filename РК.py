import random

# Создание матрицы с заданными значениями
def create_matrix(rows, cols):
    matrix = [[random.choice([1]) for _ in range(cols)] for _ in range(rows)]
    t: int = 0
    while (t < 24/3):
         no_apple_row = random.randint(0, rows - 1)
         no_apple_col = random.randint(0, cols - 1)
         matrix[no_apple_row][no_apple_col] = 0
         t += 1
    bad_apple_row = random.randint(0, rows - 1)
    bad_apple_col = random.randint(0, cols - 1)
    matrix[bad_apple_row][bad_apple_col] = 2
    return matrix

# Вывод матрицы на экран
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Функция обновления матрицы каждую минуту
def update_matrix(matrix, rows, cols):
    changed = False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2:
                if i > 0 and matrix[i-1][j] == 1:
                    matrix[i-1][j] = 2
                    changed = True
                if i < rows-1 and matrix[i+1][j] == 1:
                    matrix[i+1][j] = 2
                    changed = True
                if j > 0 and matrix[i][j-1] == 1:
                    matrix[i][j-1] = 2
                    changed = True
                if j < cols-1 and matrix[i][j+1] == 1:
                    matrix[i][j+1] = 2
                    changed = True
    return changed


# Функция поиска минимального количества минут
def find_min_minutes(matrix, rows, cols):
    minutes = 0
    while True:
        changed = update_matrix(matrix, rows, cols)
        if not changed:
            return minutes if any(1 or 2 in row for row in matrix) else -1
        minutes += 1

# Размеры матрицы
N = 5
M = 5

# Создание и вывод матрицы
matrix = create_matrix(N, M)
print("Исходная матрица:")
print_matrix(matrix)


# Нахождение минимального количества минут и вывод результата
result = find_min_minutes(matrix, N, M)
print("Минимальное количество минут:", result)
