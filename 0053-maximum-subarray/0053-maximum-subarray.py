class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=float('-inf')
        # start_subarray,end_subarray=-1,-1
        # start=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
                # start_subarray,end_subarray=start,i
            if sum<0:
                sum=0
                # start=i+1
        return maxi