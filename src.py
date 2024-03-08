def time_to_paint(K, T, L):
    if any(l < 0 for l in L):
        print("[ERROR]: Довжини щитів не можуть бути від'ємними!!!!!")
        return
    if not L:
        return 0
    L.sort(reverse=True)
    painters_time = [0] * K
    for length in L:
        min_time_index = painters_time.index(min(painters_time))
        painters_time[min_time_index] += length * T
    return max(painters_time)


def main():
    K = int(input("Кількість малярів: "))
    T = int(input("Час на замалювання 1 м щита (в хв): "))
    L = list(map(int, input("Довжини щитів (через пробіл): ").split()))
    result = time_to_paint(K, T, L)
    if result is not None:
        print("Результат для усіх:", result, "хвилин")


if __name__ == "__main__":
    main()
