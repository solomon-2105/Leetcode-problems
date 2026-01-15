class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # a = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         ai = set()
        #         for k in range(j+1,len(nums)):
        #             quad = target-(nums[i]+nums[k]+nums[j])
        #             if quad in ai:
        #                 b = tuple(sorted([nums[i],nums[j],nums[k],quad]))
        #                 a.add(b)
        #             ai.add(nums[k])
        # return [list(i) for i in a]
        nums.sort()
        a = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]: continue
                temp = nums[i]+nums[j]
                
                left , right = j+1 , n-1
                while left < right:
                    t= temp + nums[right] + nums[left]
                    if t == target:
                        a.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif t > target:
                        right -= 1
                    else:
                        left += 1 
        return a