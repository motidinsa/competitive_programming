def countSwaps(a):
    swapCount = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapCount += 1
    print(f'Array is sorted in {swapCount} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a) - 1]}')


countSwaps([3, 6, 4, 1, 2])
