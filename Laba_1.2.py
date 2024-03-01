def sort(left, array, right):
    if left < right:
        partition_pos = partition(left, array, right)
        sort(left, array, partition_pos - 1)
        sort(partition_pos + 1, array, right)


def partition(left, array, right):
    i = left
    j = right - 1
    p = array[right]

    while i < j: 
        while i < right and array[i] < p:
            i += 1
        while j > left and array[j] >= p:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > p:
        array[i], array[right] = array[right], array[i]

    return i


array = [15, 7, 22, 9, 36, 2, 42, 18]
sort(0, array, len(array) - 1)
print(array)

k = int(input())


def error(k, num):
    if k < 1 or k > len(array):
        return ValueError


def k_founder(array, k):
    left = 0
    right = len(array) - 1
    
    while True:
        pivot_index = partition(left, array, right)
        if pivot_index == len(array) - k:
            return array[pivot_index], pivot_index + 1
        elif pivot_index < len(array) - k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1


result, position = k_founder(array, k)
print(f"Знайдений {k}-й за величиною елемент: {result}")
print(f"Позиція {k}-го найбільшого елемента: {position}")