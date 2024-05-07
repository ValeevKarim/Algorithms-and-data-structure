from math import factorial


def d(n):
    if n == 1:
        return 0
    if n == 0:
        return 1
    return n * d(n-1) + (-1)**n


def c(n, k):
    return factorial(n) / factorial(n-k) / factorial(k)


n = int(input())
k = int(input())
print(c(n, k) * d(n-k))

# time and memory: O(n*(n-k))
