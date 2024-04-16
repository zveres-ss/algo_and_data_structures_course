array = [15, 7, 22, 9, 36, 2, 42, 18]
sorted_array = array.copy()

def sort(left, sorted_array, right):
    if left < right:
        partition_pos = partition(left, sorted_array, right)
        sort(left, sorted_array, partition_pos - 1)
        sort(partition_pos + 1, sorted_array, right)


def partition(left, sorted_array, right):
    i = left
    j = right - 1
    p = sorted_array[right]

    while i < j: 
        while i < right and sorted_array[i] < p:
            i += 1
        while j > left and sorted_array[j] >= p:
            j -= 1

        if i < j:
            sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]

    if sorted_array[i] > p:
        sorted_array[i], sorted_array[right] = sorted_array[right], sorted_array[i]

    return i

sort(0, sorted_array, len(sorted_array) - 1)
print(sorted_array)

k = int(input())

def error(k, num):
    if k < 1 or k > len(array):
        return ValueError

def k_founder(array, k):
    nums_sorted = sorted(array, reverse=True)
    k_largest = nums_sorted[k - 1]
    index = array.index(k_largest)
    return k_largest, index


result, position = k_founder(array, k)
print(f"Знайдений {k}-й за величиною елемент: {result}")
print(f"Позиція {k}-го найбільшого елемента: {position}")
