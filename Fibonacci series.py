def fibo():
    n = int(input('Enter the number > 0: '))

    f1 = 0
    f2 = 1
    li = []
    for i in range(n):
        li.append(f1)
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return li

result = fibo()
print(*result)
