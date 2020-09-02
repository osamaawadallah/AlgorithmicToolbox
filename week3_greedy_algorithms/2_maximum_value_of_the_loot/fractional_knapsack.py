# Uses python3
from random import randint


def get_optimal_value(capacity, values):
    tValue = 0.
    for w, v in sorted(values.items(), key=lambda x: x[1], reverse=True):
        if capacity <= 0:
            return tValue
        curWeight = min(capacity, w)
        tValue += curWeight * v
        capacity -= curWeight

    return tValue


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    value={}
    for i in range(n):
        v, w = map(int, input().split())
        value[w] = v/w
    opt_value = get_optimal_value(capacity, value)
    print("{:.10f}".format(opt_value))
