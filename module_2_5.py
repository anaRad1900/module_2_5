def get_matrix(n, m, value):
    # Проверка на корректные значения n и m
    if n <= 0 or m <= 0:
        return []  # Возвращаем пустой список при некорректных значениях

    matrix = []  # Создаем пустой список для матрицы

    # Внешний цикл для строк
    for _ in range(n):
        row = []  # Создаем пустой список для строки
        # Внутренний цикл для столбцов
        for _ in range(m):
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу

    return matrix  # Возвращаем готовую матрицу

# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)