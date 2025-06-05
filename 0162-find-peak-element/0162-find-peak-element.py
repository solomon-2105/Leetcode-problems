class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=0,len(nums)-1
        while i<j:
            m=i+(j-i)//2
            if nums[m]>nums[m+1]:
                j=m
            else:
                i=m+1
        return i
