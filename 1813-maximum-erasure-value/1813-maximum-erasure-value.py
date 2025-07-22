class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxx,summ,left=0,0,0
        brr=set()
        for i in range(len(nums)):
            while nums[i] in brr:
                summ-=nums[left]
                brr.remove(nums[left])
                left+=1
            brr.add(nums[i])
            summ+=nums[i]
            maxx=max(maxx,summ)
        return maxx