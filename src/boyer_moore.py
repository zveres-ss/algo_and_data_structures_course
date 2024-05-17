def boyer_moore_search(haystack, needle):
    if not needle:
        return []

    n = len(haystack)
    m = len(needle)
    if m > n:
        return []

    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(needle[i])] = i

    shifts = []
    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and needle[j] == haystack[s + j]:
            j -= 1

        if j < 0:
            shifts.append(s)
            s += (m - bad_char[ord(haystack[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(haystack[s + j])])

    return shifts
