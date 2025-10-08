class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        summ=0
        maxi=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ-k in a:
                maxi+=a[summ-k]
            if summ in a:
                a[summ]+=1
            else:
                a[summ]=1
        return maxi