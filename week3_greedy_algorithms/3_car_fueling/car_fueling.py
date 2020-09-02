# python3
import sys


def compute_min_refills(distance, tank, stops):
    start = 0
    end = 0
    i = 0
    while end < distance:
        while end-start <= tank:
            if i == len(stops)-1:
                break
            if stops[i]-start <= tank:
                end = start
            else:
                return -1
        
    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(d, m, stops)
    print(compute_min_refills(d, m, stops))
