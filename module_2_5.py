def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])  # добавляем список
        for j in range(m):
            matrix[i].append(value)  # Пишем в список значение

    print(matrix)
    return matrix


n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))
value = int(input("Введите значение для списка: "))

if n <= 0 or m <= 0:
    print('Вы ввели ноль строк или ноль столбцов, данные отображаться не будут')
else:
    result = get_matrix(n, m, value)
    print("Матрица:", result)
