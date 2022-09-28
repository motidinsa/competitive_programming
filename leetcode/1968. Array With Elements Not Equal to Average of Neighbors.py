class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums


print(Solution().rearrangeArray([3, 4, 0, 2, 5]))
