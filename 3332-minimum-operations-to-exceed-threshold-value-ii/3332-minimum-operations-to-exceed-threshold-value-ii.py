import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        count=0
        while nums[0]<k:
            if len(nums) >= 2:
                a=heapq.heappop(nums)
                b=heapq.heappop(nums) 
                heapq.heappush(nums,(min(a,b)*2)+max(a,b))
                count+=1
        return count