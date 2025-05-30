from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = float('-inf')
        index = -1
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                index = i
        for i in range(len(nums)):
            if nums[i] == maxi:
                continue
            if nums[i]*2 > maxi:
                return -1
        return index
