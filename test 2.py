def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
    sorted_array = []
    n = len(heights)
    for i in range(n):
        sorted_array.append([heights[i], names[i]])
    sorted_array.sort(reverse=True)
    a = []
    for i in range(n):
        a.append(sorted_array[i][1])
    return a


print(sortPeople(0, names = ["Mary","John","Emma"], heights = [180,165,170]))
