class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        count=0
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for k,v in a.items():
            if v> len(nums)//2: return k