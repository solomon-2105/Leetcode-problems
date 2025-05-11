class Solution:
    def maxProduct(self, nums):
        # Initialize max_so_far, min_so_far, and result with the first element
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            # Temporarily store the current max and min before updating
            temp_max = max(current, max_so_far * current, min_so_far * current)
            temp_min = min(current, max_so_far * current, min_so_far * current)

            # Update max_so_far and min_so_far for the next iteration
            max_so_far = temp_max
            min_so_far = temp_min

            # Update the result with the maximum product found so far
            if max_so_far > result:
                result = max_so_far

        return result
