class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # Create an empty set
        for num in nums:
            if num in seen:  # If the number is already in the set, return True
                return True
            seen.add(num)  # Otherwise, add it to the set
        return False  # No duplicates found
