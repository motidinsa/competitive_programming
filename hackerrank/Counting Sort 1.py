def countingSort(arr):
    a = [0] * 100
    for i in range(len(arr)):
        a[arr[i]] += 1
    return a

