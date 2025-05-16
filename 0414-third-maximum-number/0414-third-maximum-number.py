import sys
class Solution:
    def thirdMax(self, nums):
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

        return first if third == -float('inf') else third