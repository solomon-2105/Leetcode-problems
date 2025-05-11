class Solution:
    def maxSubArray(self, nums):
        sum = 0
        maxi = float('-inf')  # Equivalent to INT_MIN
        for i in range(len(nums)):
            sum += nums[i]
            maxi = max(maxi, sum)
            if sum < 0:
                sum = 0

        return maxi
