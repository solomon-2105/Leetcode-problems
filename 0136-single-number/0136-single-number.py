class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        brr=0
        for i in nums:
            brr^=i
        return brr