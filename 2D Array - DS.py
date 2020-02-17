arr = [ [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
      ]

res = []
for row in range(len(arr)-2):
    for column in range(len(arr)-2):
        r1 = arr[row][column]
        r2 = arr[row][column + 1]
        r3 = arr[row][column + 2]
        r4 = arr[row + 1][column + 1]
        r5 = arr[row + 2][column]
        r6 = arr[row + 2][column + 1]
        r7 = arr[row + 2][column + 2]
        res.append(r1 + r2 + r3 + r4 + r5 + r6 + r7)

print(max(res))