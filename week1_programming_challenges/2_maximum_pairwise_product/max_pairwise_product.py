# python3
from random import randrange

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    temp = numbers[:]
    max_product = 0
    max1 = max(temp)
    temp.remove(max1)
    max2 = max(temp)
    max_product = max1 * max2
    return max_product

while True:
    n = randrange(10) + 2
    numbers = []
    print(n)
    for num in range(n):
        numbers.append(randrange(100000))
    print(numbers)

    res1 = max_pairwise_product(numbers)
    res2 = max_pairwise_product_fast(numbers)
    if res1 == res2:
        print(f"OK, result is {res1}")
    else:
        print(f"Error: {res1} != {res2}")
        break

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
