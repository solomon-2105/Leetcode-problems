from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Total distinct elements in the whole array
        D = len(set(nums))
        n = len(nums)
        
        freq = defaultdict(int)
        count = 0
        left = 0
        distinct_in_window = 0
        
        # Slide 'right' from 0 to n-1
        for right in range(n):
            # Include nums[right] into the window
            if freq[nums[right]] == 0:
                distinct_in_window += 1
            freq[nums[right]] += 1
            
            # Once our window [left..right] has all D distinct values,
            # we can start moving 'left' forward to count subarrays.
            while distinct_in_window == D:
                # All subarrays starting at any index from 'left' to 'right'
                # and ending at 'right' are complete.
                # That’s exactly (n - right) subarrays ending at right.
                count += (n - right)
                
                # Now shrink the window from the left
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_in_window -= 1
                left += 1
        
        return count
