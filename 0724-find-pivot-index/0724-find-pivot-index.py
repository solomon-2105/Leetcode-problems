class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum=0
        brr=sum(nums)
        for i in range(len(nums)):
            if presum==brr-presum-nums[i]:
                return i
            presum+=nums[i]
        return -1