class Solution:
    def maxKDistinct(self, nums, k):
        nums.sort(reverse=True)
        res=[nums[0]]
        k-=1
        i=1
        while k>0 and i<len(nums):
            if nums[i]!=nums[i-1]:
                res.append(nums[i])
                k-=1
            i+=1
        return res
