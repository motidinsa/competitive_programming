class Solution(object):
    def kthLargestNumber(self, nums, k):
        numArray = []
        for i in range(len(nums)):
            numArray.append(int(nums[i]))
        numArray.sort()
        return str(numArray[len(nums) - k])


print(Solution().kthLargestNumber(["3", "6", "7", "10"], 4))
