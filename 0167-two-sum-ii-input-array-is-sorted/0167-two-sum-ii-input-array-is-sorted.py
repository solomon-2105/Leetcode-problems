class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a,b=0,len(nums)-1
        while a<b:
            c=nums[a]+nums[b]
            if c==target:
                return [a+1,b+1]
            elif c>target:
                b-=1
            else:
                a+=1
        return [-1,-1]