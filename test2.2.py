n = int(input())
w = int(input())
h = int(input())
l = 0
r = max(w, h) * n
while l < r:
    m = (l+r) // 2
    if (m // h) * (m // w) < n:
        l = m + 1
    else:
        r = m
print(r)
