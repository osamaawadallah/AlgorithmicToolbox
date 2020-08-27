# Uses pytho

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def find_redundancy(n, m):
    cond = False
    for i in range(1000*m):
        if i == 0:
            continue
        if cond and get_fibonacci_huge_naive(i, m) == 1:
            break
        else:
            cond = False
        if get_fibonacci_huge_naive(i, m) == 0:
            cond = True
    return (i - 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    red = find_redundancy(n, m)
    print(get_fibonacci_huge_naive(n % red, m))
