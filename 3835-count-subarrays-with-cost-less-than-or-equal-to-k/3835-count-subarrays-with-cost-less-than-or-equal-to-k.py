from collections import deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # maxi , mini = 0 , (10**9) + 1
        # count = 0 
        # for i in range(len(nums)):
        #     maxi = nums[i]
        #     mini = nums[i]
        #     for j in range(i, len(nums)):
        #         if nums[j] > maxi:
        #             maxi = nums[j]
        #         if nums[j] < mini:
        #             mini = nums[j]
        #         cost = (maxi - mini) * (j - i + 1)
        #         if cost <= k:
        #             count += 1
        # return count
        maxq = deque()
        minq = deque()
        i , ans = 0 , 0
        for j in range(len(nums)):
            
            while maxq and nums[maxq[-1]] <= nums[j]:
                maxq.pop()
            maxq.append(j)
            
            while minq and nums[minq[-1]] >= nums[j]:
                minq.pop()
            minq.append(j)

            while (nums[maxq[0]]  - nums[minq[0]]) * (j - i + 1) > k:
                if maxq[0] == i:
                    maxq.popleft()
                if minq[0] == i:
                    minq.popleft()
                i += 1

            ans += (j-i+1)
        return ans