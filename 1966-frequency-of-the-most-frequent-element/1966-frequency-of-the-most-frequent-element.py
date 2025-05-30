class Solution(object):
    def maxFrequency(self,nums,k):
        nums.sort()
        l=0
        total=0
        maxFreq=0
        for r in range(len(nums)):
            total+=nums[r]
            while (r-l+1)*nums[r]-total>k:
                total-=nums[l]
                l+=1
            maxFreq=max(maxFreq,r-l+1)
        return maxFreq