class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a,b=0,len(nums)
        while a<b:
            mid=a + ((b-a)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                a=mid+1
            elif nums[mid]>target:
                b=mid
        return a