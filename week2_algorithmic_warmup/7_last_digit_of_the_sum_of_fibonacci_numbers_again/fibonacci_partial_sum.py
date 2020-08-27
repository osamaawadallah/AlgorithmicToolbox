# Uses python3
def sum(n):
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

    if n == 0:
        return 0
    else:
        return fibonacci_sum_naive(n) % find_redun(n)


if __name__ == '__main__':
    from_, to = map(int, input().split())
    num1 = sum(to)
    num2 = sum(from_ - 1)
    if num2 > num1:
        num1 += 10

    print((num1-num2)%10)