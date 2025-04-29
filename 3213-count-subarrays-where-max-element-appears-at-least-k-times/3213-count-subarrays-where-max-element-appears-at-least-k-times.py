class Solution:
    def countSubarrays(self,nums:List[int],k:int)->int:
        m=max(nums)
        l=0
        cnt=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==m: cnt+=1
            while cnt>=k:
                ans+=len(nums)-r
                if nums[l]==m: cnt-=1
                l+=1
        return ans
