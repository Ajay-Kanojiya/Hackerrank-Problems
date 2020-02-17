def countSwaps(a):
    count = 0
    for x in range(len(a) - 1):
        for y in range((len(a) - 1) - x):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]
                count += 1
    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(count, a[0], a[-1]))


countSwaps([3, 2, 1])
