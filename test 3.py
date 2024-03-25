def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    items1.sort()
    items2.sort()
    i, j = 0, 0
    ret = []
    n, m = len(items1), len(items2)
    while i < n and j < m:
        if items1[i][0] < items2[j][0]:
            ret.append(items1[i])
            i += 1
        elif items1[i][0] > items2[j][0]:
            ret.append(items2[j])
            j += 1
        else:
            ret.append([items2[j][0], items2[j][1] + items1[i][1]])
            i += 1
            j += 1
    while i < n:
        ret.append(items1[i])
        i += 1
    while j < m:
        ret.append(items2[j])
        j += 1
    return ret

print(mergeSimilarItems(0, items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))