class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
         
        # bruteforce  (tle for 22 testcases'
        # for i in range(len(nums)) : 
        #     for j in range(i+1 , len(nums)):
        #         c = j - i + 1 
        #         com = 0
        #         for p in range(i , j + 1):
        #             com += nums[p]
        #         if (c >= 2) and (com % k == 0):
        #             return True
        # return False

        #optimal (using prefix hashmap approach)
        hashmap = {0 : -1}
        com = 0
        for i , j in enumerate(nums):
            com += j
            com %= k
            if com in hashmap :
                if i - hashmap[com] > 1:
                    return True
            else:
                hashmap[com] = i
        return False