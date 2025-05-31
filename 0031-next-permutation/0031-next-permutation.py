class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pivot=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot==-1:
            nums.reverse()
            return
        for i in range(n-1,-1,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        i,j=pivot+1,n-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1