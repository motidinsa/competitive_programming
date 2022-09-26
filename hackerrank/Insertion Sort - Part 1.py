def insertionSort1(n, arr):
    lastNum = arr[n - 1]
    i = n - 1
    while i >= 0:
        if lastNum < arr[i - 1] and i != 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i - 1]
            i -= 1
            print(' '.join(map(str, arr)))

        else:
            arr[i] = lastNum
            print(' '.join(map(str, arr)))
            break


insertionSort1(5, [2, 4, 6, 8, 1])
