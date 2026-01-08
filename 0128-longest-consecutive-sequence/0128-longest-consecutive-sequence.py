class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = cur = 0
        a = set(nums)
        for i in a:
            if i-1 not in a:
                cur = 1
                while i+cur in a:
                    cur+=1
                maxi = max(maxi , cur)
        return maxi