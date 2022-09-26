class Solution:
    def select(self, arr, i):
        return arr[i:]

    def selectionSort(self, arr, n):

        for i in range(len(arr)):
            currentMin = arr[i]
            for j in range(i + 1, len(arr)):
                if arr[j] < currentMin:
                    currentMin = arr[j]
                    arr[i], arr[j] = currentMin, arr[i]
        return arr


print(Solution().selectionSort([2, 4, 3, 1], 1))
