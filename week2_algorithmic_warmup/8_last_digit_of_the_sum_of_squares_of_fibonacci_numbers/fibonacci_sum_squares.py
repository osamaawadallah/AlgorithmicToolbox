# Uses python3

def answer(n):
    def get_fibonacci_last_digit_naive(n):
        if n <= 1:
            return n
        previous = 0
        current = 1
        for _ in range(n - 1):
            previous, current = current, previous + current
        return current % 10


    n %= 60
    return get_fibonacci_last_digit_naive(n)


if __name__ == '__main__':
    n = int(input())
    print((answer(n)*answer(n+1)) % 10)
