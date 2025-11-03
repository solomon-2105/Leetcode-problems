class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=None
        count=0
        i=0
        while i<len(nums):
            if count==0:
                el=nums[i]
            if nums[i]==el:
                count+=1
            else:
                count-=1
            i+=1
        # b=0
        # for i in nums:
        #     if i==el: b+=1
        # return el if b>len(nums)//2 else -1
        return el