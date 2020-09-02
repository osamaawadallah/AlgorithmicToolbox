# Uses python3

def get_change(m):
    #write your code here
    temp = m
    count = 0
    coin = [10, 5, 1]
    for i in range(3):
        count += temp // coin[i]
        temp %= coin[i]
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
