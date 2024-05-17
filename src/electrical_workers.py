import math

def max_wire_length(w, heights):
    n = len(heights)
    total_length = 0.0

    for i in range(n - 1):
        h1 = heights[i] if i % 2 == 0 else 1
        h2 = heights[i + 1] if (i + 1) % 2 == 0 else 1
        distance = math.sqrt(w ** 2 + (h1 - h2) ** 2)
        total_length += distance

    return round(total_length, 2)


def main():
    w = int(input())
    heights = list(map(int, input().split()))

    result = max_wire_length(w, heights)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
