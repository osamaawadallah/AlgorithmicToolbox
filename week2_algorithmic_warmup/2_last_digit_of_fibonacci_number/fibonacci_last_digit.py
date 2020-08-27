# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10


def get_fibonacci_last_digit(n):
    n %= 60
    return get_fibonacci_last_digit_naive(n)

# for n in range(46):
#     print(n)
#     res1 = get_fibonacci_last_digit_naive[n]
#     res2 = get_fibonacci_last_digit(n)
#     if res1 == res2:
#         print("OK")
#     else:
#         print(f"Error {res1} != {res2}")
#         break


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
