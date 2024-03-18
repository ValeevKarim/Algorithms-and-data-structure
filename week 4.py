def threeSumClosest(self, A:list, B):
    n = len(A)
    if n < 3:
        return -1
    A.sort()
    minDifference = abs(A[0] + A[1] + A[2] - B)
    bestTillNow = A[0] + A[1] + A[2]
    for i in range(n):
        j = i+1
        k = n-1
        while j < k:
            current_sum = A[i] + A[j] + A[k]
            newDiff = abs(current_sum - B)
            if newDiff < minDifference:
                minDifference = newDiff
                bestTillNow = A[i] + A[j] + A[k]
            if current_sum < B:
                j += 1
            elif current_sum > B:
                k -= 1
            else:
                return B
    return bestTillNow


print(threeSumClosest(0, [ 10, -6, 3, 4, -8, -5 ], 3))

# time complexity is O(n^2)
# memory complexity is O(1)
