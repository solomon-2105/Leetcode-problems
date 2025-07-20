class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg=0,1
        brr=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]<0:
                brr[neg]=nums[i]
                neg+=2
            elif nums[i]>0:
                brr[pos]=nums[i]
                pos+=2
        return brr