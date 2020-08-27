# Uses python3
# from random import randint

# fibNum = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
#           1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
#           832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
#           102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]


def fib(n):
    if n < 2:
        return n
    n1 = 0
    n2 = 1
    for i in range(n + 1):
        if i < 2:
            continue
        n1, n2 = n2, n1 + n2
    return n2


n = int(input())
print(fib(n))

# for n in range(46):
#     print(n)
#     res1 = fibNum[n]
#     res2 = fib(n)
#     if res1 == res2:
#         print("OK")
#     else:
#         print(f"Error {res1} != {res2}")
#         break
