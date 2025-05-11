class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
