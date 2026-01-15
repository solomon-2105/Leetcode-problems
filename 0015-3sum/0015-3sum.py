class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a = set()
        # for i in range(len(nums)):
        #     brr = set()
        #     for j in range(i+1,len(nums)):
        #         k = -1 * (nums[i]+nums[j])
        #         if k in brr:
        #             tri = tuple(sorted([nums[i],nums[j],k]))
        #             a.add(tri)
        #         brr.add(nums[j])    
        # return [list(i) for i in a]

        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left , right = i+1 , len(nums)-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    ans.append([nums[i],nums[right],nums[left]])
                    left+=1
                    right-=1 

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif temp>0:
                    right-=1
                else:
                    left+=1
        return ans