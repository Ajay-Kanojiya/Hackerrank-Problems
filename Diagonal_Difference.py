def digdiff():
    diagonal1, diagonal2 = 0, 0
    for i in range(len(arr)):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][len(arr) - 1 - i]
    return abs(diagonal1 - diagonal2)


n = int(input('Enter the number of rows:'))
arr = []
for i in range(n):
    arr.append(list(map(int, input('Enter the elements:').rstrip().split())))
print(arr)
result = digdiff()
print(result)
