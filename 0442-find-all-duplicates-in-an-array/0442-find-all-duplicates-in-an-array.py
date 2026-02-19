class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # All numbers are in the range 1 to n.
        # So each number can point to an index (number - 1).
        
        # If we visit a number for the first time,
        # we make the value at its index negative to mark it.
        # If we see that index already negative,
        # it means the number has appeared before indicating it's a duplicate.

        a = []
        
        for i in range(len(nums)):
            # Get the correct index using absolute value
            # (because it might already be negative).
            r = abs(nums[i]) - 1
            
            # If already negative, number is duplicate.
            if nums[r] < 0:
                a.append(r + 1)
            
            # Otherwise mark it as visited.
            else:
                nums[r] *= -1
        
        # Return all duplicates found.
        return a
