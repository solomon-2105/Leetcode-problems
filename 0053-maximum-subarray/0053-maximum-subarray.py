class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current_sum keeps track of the running sum of the current subarray.
        # max_sum stores the largest sum found so far.
        
        current_sum = 0
        max_sum = float('-inf')
        
        for i in range(len(nums)):
            # Add current number to the running sum.
            current_sum += nums[i]
            
            # If current running sum is greater than max_sum,
            # update max_sum.
            if current_sum > max_sum:
                max_sum = current_sum
            
            # If running sum becomes negative,
            # reset it to 0 because a negative sum
            # will only reduce future subarray sums.
            if current_sum < 0:
                current_sum = 0
        
        # max_sum is the maximum subarray sum.
        return max_sum