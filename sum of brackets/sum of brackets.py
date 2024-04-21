import math

def bracket_sum(n, x):
    result = 0
    for i in range(n):
        result += math.floor(x + i / n)
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    x = float(input())
    print(bracket_sum(n, x))