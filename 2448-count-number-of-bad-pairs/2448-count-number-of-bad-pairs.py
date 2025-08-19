class Solution:
    def countBadPairs(self, nums):
        count = {}  # Dictionary to store frequency of (nums[i] - i)
        good_pairs = 0  # Count of good pairs
        n = len(nums)  # Store length to avoid repeated calculations

        for i in range(n):
            diff = nums[i] - i  # Compute the difference
            if diff not in count:
                count[diff] = 0
            good_pairs += count[diff]  # Add previous occurrences
            count[diff] += 1  # Update dictionary

        total_pairs = n * (n - 1) / 2  # Use `/` instead of `//` in Python 2
        return int(total_pairs - good_pairs)  # Convert to int for Python 2 compatibility
