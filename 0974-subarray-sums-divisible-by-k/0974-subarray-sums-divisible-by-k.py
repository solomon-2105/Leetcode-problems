class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #bruteforce (38/76) , (66/76)
        # c = 0
        # n = len(nums)
        # prefix = [0] * n
        # prefix[0] = nums[0]
        # for i in range(1,n):
        #     prefix[i] = prefix[i-1] + nums[i]
        # summation = 0
        # for i in range(n):
        #     for j in range(i , n):
        #         if i == 0 :
        #             summation = prefix[j]
        #         else:
        #             summation = prefix[j] - prefix[i-1]
        #         if summation % k == 0:
        #             c += 1
        # return c

        hashmap = {0:1}
        n = len(nums)
        presum = 0
        c = 0
        for i in range(n):
            presum += nums[i]
            presum %= k
            if presum in hashmap:
                c += hashmap[presum]
            hashmap[presum] = hashmap.get(presum , 0) + 1
        return c