class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt,ls,longest,a=0,float('-inf'),0,len(nums)
        for i in range(a):
            if nums[i]-1==ls:
                cnt+=1
                ls=nums[i]
            elif nums[i]!=ls:
                cnt=1
                ls=nums[i]
            longest=max(longest,cnt)
        return longest