import sys
class Solution:
    def thirdMax(self, nums):
        first = -sys.maxsize - 1
        second = -sys.maxsize - 1
        third = -sys.maxsize - 1

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

        return first if third == -sys.maxsize - 1 else third
