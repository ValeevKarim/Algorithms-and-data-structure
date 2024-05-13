def f(n, lst):
    res = []

    def backtrack(x, s1, s2):
        if x == n:
            res.append(abs(s1-s2))
        else:
            backtrack(x+1, s1+int(lst[x][1:]), s2)
            backtrack(x + 1, s1, s2 + int(lst[x][1:]))

    backtrack(0, 0, 0)

    return min(res)


A = ['W1', 'W2', 'W3', 'W105']
print(f(4, A))
