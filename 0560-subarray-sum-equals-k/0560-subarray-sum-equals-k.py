class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={}
        summ=0
        maxi=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ==k:
                maxi=max(maxi,i+1)
            if summ-k in a:
                maxi=max(maxi,i-a[summ-k])
            if summ not in a:
                a[summ]=i
        return maxi