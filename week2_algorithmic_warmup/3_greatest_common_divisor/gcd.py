# Uses python3
import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    a /= b
    return gcd_naive(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if b > a:
        a, b = b, a
    print(gcd_naive(a, b))
