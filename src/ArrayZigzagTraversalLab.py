# Рівень 3.
# Варіант 1
# Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу".
# Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву,
# починаючи з лівої верхньої точки. Другим елементом буде виведено елемент, який знаходиться справа,
# потім знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо.
# Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так
# (де номер у клітинці відповідає порядку її відвідин):
# 1 2 6 3 5 7 4 8 9
# Для масиву 3 х 5 це матиме вигляд:
# 1 2 6 7 12 3 5 8 11 13 4 9 10 14 15
# Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та
# поверне одномірний масив з значеннями елементів вхідного масиву при обході
# його у порядку, зазначеному вище у задачі.

# діагональ вправо-вгору, межі - до верху масиву (і = 0)
def diag_up(i, j, n, m, arr, result_arr):
    while 0 < i <= n - 1 and 0 <= j <= m - 2:
        i -= 1
        j += 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


# діагональ вліво-вниз, межі - до лівого краю масиву (j = 0)
def diag_down(i, j, n, m, arr, result_arr):
    while 0 <= i <= n - 2 and 0 < j <= m - 1:
        i += 1
        j -= 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def go_left(i, j, n, m, arr, result_arr):
    if 0 < j <= m - 1:
        j -= 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def go_up(i, j, n, m, arr, result_arr):
    if i != 0:
        i -= 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def arr_zigzag_traverse(arr, n, m):
    result_arr = []
    # ЛОКАЛЬНІ і та j це значення індексів в масиві, де і відповідає за ряки (n)
    # а j - за стовпці (m)
    i = n - 1
    j = m - 1
    curr_val = arr[i][j]    # поточне значення (1), записується в одновимірний масив
    result_arr.append(curr_val)

    # якшо масив де-факто одновимірний то виводим його
    if m == 1:
        for i in range(1, len(arr)):
            result_arr.append(arr[i])
        return result_arr

    # цикл дійсний поки і в межах рядків, а j - в межах стовпців
    while 0 <= i <= n - 1 and 0 <= j <= m - 1:
        # якшо стоїмо на передостанньому елементі,
        # просто рухаємся вліво і виходим
        if i == 0 and j == 1:
            go_left(i, j, n, m, arr, result_arr)
            return result_arr

        elif i == n - 1 and 0 < j <= m - 1:
            i, j = go_left(i, j, n, m, arr, result_arr)
            i, j = diag_up(i, j, n, m, arr, result_arr)

        elif 0 < i <= n - 1 and j == m - 1:
            i, j = go_up(i, j, n, m, arr, result_arr)
            i, j = diag_down(i, j, n, m, arr, result_arr)

        elif 0 < i <= n - 1 and j == 0:
            i, j = go_up(i, j, n, m, arr, result_arr)
            i, j = diag_up(i, j, n, m, arr, result_arr)

        elif i == 0:
            i, j = go_left(i, j, n, m, arr, result_arr)
            i, j = diag_down(i, j, n, m, arr, result_arr)


# Для перевірки виконання роботи реалізованого алгоритму
# слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму
# при значеннях m == n == 5, m = 2, n = 4, n = 1, m = 6, n == m == 1