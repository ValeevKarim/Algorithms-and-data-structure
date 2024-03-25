def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    new_arr = []
    mx = max(candies)
    for i in range(len(candies)):
        new_arr.append(candies[i] + extraCandies >= mx)
    return new_arr


print(kidsWithCandies(0, [4,2,1,1,2], 1))