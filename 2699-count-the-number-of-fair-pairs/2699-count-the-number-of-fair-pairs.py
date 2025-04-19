from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            min_needed = lower - nums[i]
            max_needed = upper - nums[i]

            # Only search in the range (i+1 to end), since j > i
            left = bisect_left(nums, min_needed, i + 1, n)
            right = bisect_right(nums, max_needed, i + 1, n)

            count += (right - left)

        return count
