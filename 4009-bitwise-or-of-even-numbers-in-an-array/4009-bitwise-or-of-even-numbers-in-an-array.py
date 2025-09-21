class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if i%2==0:
                s=s|i
        return s