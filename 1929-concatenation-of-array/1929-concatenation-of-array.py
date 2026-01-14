class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # a=[0]*(2*n)
        # for i in range(n):
        #     a[i]=nums[i]
        #     a[i+n]=nums[i]
        # return a
        return nums*2