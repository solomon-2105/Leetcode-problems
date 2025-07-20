class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=None
        c=0
        for i in nums:
            if c==0:
                el=i
                c=1
            elif el==i:
                c+=1
            else:
                c-=1
        brr=0
        for i in nums:
            if i==el: brr+=1
        if brr> len(nums)//2: return el
         
