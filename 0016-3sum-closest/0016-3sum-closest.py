class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        brr=float('inf')
        grr=float('inf')
        for i in range(len(nums)-2):
            a,b=i+1,len(nums)-1
            while a<b:
                c=nums[i]+nums[a]+nums[b]
                d=abs(c-target)
                if d<grr:
                    grr=d
                    brr=c
                if c<target:
                    a+=1
                else:
                    b-=1
        return brr