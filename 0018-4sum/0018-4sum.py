class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ai = set()
                for k in range(j+1,len(nums)):
                    quad = target-(nums[i]+nums[k]+nums[j])
                    if quad in ai:
                        b = tuple(sorted([nums[i],nums[j],nums[k],quad]))
                        a.add(b)
                    ai.add(nums[k])
        return [list(i) for i in a]