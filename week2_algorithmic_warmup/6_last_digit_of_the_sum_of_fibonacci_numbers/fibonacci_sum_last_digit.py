# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def find_redun(n):
    if n == 0:
        return n
    for i in range(1000*n):
        if i > 0:
            if fibonacci_sum_naive(i) == 0 and fibonacci_sum_naive(i+1) == 1:
                return i


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(fibonacci_sum_naive(n) % find_redun(n))
