class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        s = [0,0]
        a = 0
        for i , j in enumerate(nums):
            if j%2 == 1:
                a ^= 1
            if i%6 == 5:
                a ^= 1
            s[a] += j
        return s[0] - s[1]