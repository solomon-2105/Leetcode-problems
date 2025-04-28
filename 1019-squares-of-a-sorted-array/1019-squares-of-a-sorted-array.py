class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,l=0,0
        j,r=len(nums)-1,len(nums)-1
        brr=[0]*len(nums)
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                brr[r]=nums[j]**2
                j-=1
            else:
                brr[r]=nums[i]**2
                i+=1
            r-=1
        return brr