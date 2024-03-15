N = 5

def check_sections(N):
    if N >= 100000:
        print("Ви не мільйонер, не брешіть")
    elif N <= 2:
        print("Секцій, не секція, щоби вирішити данну проблему вам потрібно 3 секції")

check_sections(N)

C = 3

def check_numbers_of_cows(C, N):
    if C >= N:
        print("Якби у вас корів було більше секцій, ви би в любому випадку не вирішили би проблему))")
    if C <= 2:
        print("Хіба на м'ясо пускайте")

check_numbers_of_cows(C, N)

free_sections = [1, 2, 8, 4, 9]

def sort(first, free_sections, last):
    if first < last:
        sort_partition_pos = sort_partition(first, free_sections, last)
        sort(first, free_sections, sort_partition_pos - 1)
        sort(sort_partition_pos + 1, free_sections, last)

def sort_partition(first, free_sections, last):
    i = first
    j = last - 1
    piv = free_sections[last]

    while i < j:
        while i < last and free_sections[i] < piv:
            i += 1
        while j > first and free_sections[j] >= piv:
            j -= 1

        if i < j:
            free_sections[i], free_sections[j] = free_sections[j], free_sections[i]

    if free_sections[i] > piv:
        free_sections[i], free_sections[last] = free_sections[last], free_sections[i]

    return i

sort(0, free_sections, len(free_sections) - 1)

def check_placing_cows(free_sections, min_distance, happy_cows):
    F = len(free_sections)
    happy_cows = 1
    last_c = free_sections[0]

    for i in range(1, F):
        if free_sections[i] - last_c >= min_distance:
            happy_cows += 1
            last_c = free_sections[i]
        else:
            continue
        if happy_cows == C:
            return True
    return False

def search(C, F):
    left = 1
    right = free_sections[F - 1] - free_sections[0]

    while left <= right:
        mid = (left + right) // 2
        if check_placing_cows(free_sections, mid, C):
            left = mid + 1
        else:
            right = mid - 1

    return right

b_search = search(free_sections, C)

print(b_search)
