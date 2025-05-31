class Solution:
    def maxProduct(self, nums):
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, max_so_far * current, min_so_far * current)
            temp_min = min(current, max_so_far * current, min_so_far * current)
            max_so_far = temp_max
            min_so_far = temp_min
            if max_so_far > result:
                result = max_so_far
        return result