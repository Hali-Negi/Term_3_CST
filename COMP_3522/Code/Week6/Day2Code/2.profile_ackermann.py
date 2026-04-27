import sys


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


def main():
    result = ackermann(3, 7)
    # result2 = ackermann(3, 4)
    print(result)
    # print(result2)


if __name__ == "__main__":
    current = sys.getrecursionlimit()
    print(f"recursion limit {current}")
    sys.setrecursionlimit(10000)

    main()
