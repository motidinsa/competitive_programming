class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        targetIndices = []
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndices.append(i)
        return targetIndices


print(Solution().targetIndices([1, 2, 5, 2, 3], 5))
