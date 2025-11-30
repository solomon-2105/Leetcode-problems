class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==0: return n
        nums.sort()
        brr=nums[n-k]
        grr=0
        for i in nums:
            if i<brr:
                grr+=1
            else:
                break
        return grr