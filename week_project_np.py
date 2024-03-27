import numpy as np
# 1
print(np.array([0]*10), '\n')

# 2
print(np.array([5]*10), '\n')

# 3
print(np.arange(10, 51), '\n')

# 4
arr = np.arange(10, 51)
print(arr[arr % 2 == 0], '\n')

# 5
print(np.arange(9).reshape(3, -1), '\n')

# 6
print(np.identity(3), '\n')

# 7
print(np.random.randint(2), '\n')

# 8
print(np.random.randint(100, size=25), '\n')

# 9
print(np.random.random(size=20), '\n')

# 10
arr = np.array([1, 2, 3, 4])
print(arr.reshape(2, 2))

# 11
a = np.random.randint(10, size=15).reshape(5, 3)
b = np.random.randint(10, size=6).reshape(3, 2)
print(np.dot(a, b), '\n')

# 12
arr = np.arange(1, 11)
print(arr[arr % 2 == 1], '\n')

# 13
arr = np.arange(1, 11)
print(arr)
arr[arr % 2 == 1] = -1
print(arr, '\n')

# 14
arr = np.random.randint(-10, 11, size=10)
print(arr)
arr = arr > 0
print(arr, '\n')

# 15
arr = np.random.randint(11, size=10)
print(arr)
arr[arr % 2 == 0] = -arr[arr % 2 == 0]
print(arr, '\n')

# 16
arr = np.random.randint(11, size=(3, 3))
print(arr)
print(np.trace(arr), '\n')

# 17
arr = np.array([1, 2, 0, 0, 4, 0])
print(np.where(arr == 0), '\n')

# 18
arr = np.arange(1, 11)
print(arr[::-1], '\n')

# 19
print(np.identity(3), '\n')

# 20
arr = np.arange(1, 11)
print(arr.reshape(5, 2), '\n')

# 21
arr1 = np.arange(1, 11)
arr2 = np.arange(11, 21)
arr = np.stack((arr1, arr2), axis=0)
print(arr, '\n')

# 22
arr1 = np.arange(1, 11)
arr2 = np.arange(6, 11)
print(np.intersect1d(arr1, arr2), '\n')

# 23
print(np.random.randint(5, size=(5, 5)), '\n')

# 24
arr = np.random.randint(11, size=10)
print(arr)
print(arr.argmax(), '\n')

# 25
arr = np.random.randint(2, size=(3, 5))
print(arr, '\n***')
print(np.mean(arr, axis=1).reshape(3, 1), '\n')

# 26
arr = np.random.randint(11, size=(4, 4))
print(arr)
print(arr.diagonal(), '\n')

# 27
arr = np.random.randint(3, size=10)
print(arr)
print(np.count_nonzero(arr == 2), '\n')

# 28
arr1 = np.random.randint(3, size=10)
arr2 = np.random.randint(3, size=10)
print(arr1, arr2)
print(np.where(arr1 == arr2), '\n')

# 29
arr1 = np.random.randint(3, size=(2, 2))
arr2 = np.random.randint(3, size=(2, 2))
print(arr1)
print(arr2)
print(np.dot(arr1, arr2))

# 30
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
i = 0
r = []
while i < len(z)-3:
    r.append(z[i:i+4])
    i += 1
print(r, '\n')

# 31
with open('a') as file:
    s = file.readlines()
    a = []
    for i in s:
        a.append(list(map(int, i.split())))
    print(np.array(a).reshape(3, 9), '\n')
# 32
arr = np.random.random(size=(3, 3))
print(arr)
arr = arr > 0.5
newarr = arr.astype(int)
print(newarr, '\n')

# 33
arr = np.random.randint(100, size=(2, 2))
print(arr)
mx = arr.max()
a = np.where(arr == mx)
mn = arr.min()
b = np.where(arr == mn)
arr[a] = mn
arr[b] = mx
print(arr)