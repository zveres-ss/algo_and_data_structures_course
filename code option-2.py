def is_monotonic():
    while True:
        arr = input("Enter number (або Y щоб завершити):")
        if arr == ['Y']:
            break
        arr = [int(x) for x in arr]
        sorted_arr = sorted(arr)
        print("Result:", arr == sorted_arr or arr[::-1] == sorted_arr)

is_monotonic()
