import math


class Solution(object):
    def kClosest(self, points, k):
        sortedDistances = []
        unsortedDistances = []
        for i in range(len(points)):
            unsortedDistances.append([math.sqrt((points[i][0]) ** 2 + (points[i][1] ** 2)), i])
        unsortedDistances.sort()
        for i in range(k):
            sortedDistances.append(points[unsortedDistances[i][1]])
        return sortedDistances


print(Solution().kClosest([[3, 4], [1, 1]], 1))
