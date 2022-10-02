class Solution(object):
    def numIdenticalPairs(self, nums):
        goodNumPairCount = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    goodNumPairCount += 1
        return goodNumPairCount


print(Solution().numIdenticalPairs([1, 2, 3]))
