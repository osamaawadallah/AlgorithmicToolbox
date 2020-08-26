# Uses python3

n = int(input())
n1 = 0
n2 = 1
answer = n1+ n2
for i in range(n-1):
    answer = n1 + n2
    n1, n2 = n2, answer
print(answer)
