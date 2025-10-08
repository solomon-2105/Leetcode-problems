class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:-1} 
        b=0 
        c=0 
        for i in range(len(nums)):
            b+=nums[i]
            if (b-k) in a:
                c=max(c,i-a[b-k])
            if b not in a:
                a[b]=i
        return c
