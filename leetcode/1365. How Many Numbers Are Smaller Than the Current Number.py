class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smallerNumCount = [0] * len(nums)
        for i in range(len(nums)):
            currentCount = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    currentCount += 1
            smallerNumCount[i] = currentCount
        return smallerNumCount


print(Solution().smallerNumbersThanCurrent([6, 5, 4, 8]))
