def is_monotonic(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr or arr[::-1] == sorted_arr

print(is_monotonic([1,2,3,4,5]))
print(is_monotonic([5,4, 3, 2,1]))
