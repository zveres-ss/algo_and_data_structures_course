def check_sections(N):
    if N >= 100000:
        print("Ви не мільйонер, не брешіть")
    elif N <= 2:
        print("Секцій, не секція, щоби вирішити данну проблему вам потрібно 3 секції")


N = 5
check_sections(N)

C = 3


def check_numbers_of_cows(C, N):
    if C >= N:
        print(
            "Якби у вас корів було більше секцій, ви би в любому випадку не вирішили би проблему))"
        )
    if C <= 2:
        print("Хіба на м'ясо пускайте")


check_numbers_of_cows(C, N)

free_sections = [1, 2, 8, 4, 9]


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


def sort(first, free_sections, last):
    if first < last:
        sort_partition_pos = sort_partition(first, free_sections, last)
        sort(first, free_sections, sort_partition_pos - 1)
        sort(sort_partition_pos + 1, free_sections, last)


sort(0, free_sections, len(free_sections) - 1)


def rescue_cows(N, C, free_sections):
    def check_placing_cows(min_distance):
        happy_cows = 1
        last_p = free_sections[0]

        for section in free_sections[1:]:
            if section - last_p >= min_distance:
                happy_cows += 1

                if happy_cows == C:
                    return True
        return False

    left = 0
    right = free_sections[-1] - free_sections[0]
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if check_placing_cows(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

        return result


print(rescue_cows(N, C, free_sections))
