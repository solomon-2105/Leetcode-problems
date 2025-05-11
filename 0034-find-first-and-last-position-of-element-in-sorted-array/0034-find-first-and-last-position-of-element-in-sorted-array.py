class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if target not in nums:
        #     return [-1,-1]
        # a=[]
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         a.append(i)
        # return [a[0],a[-1]] 

        def left(nums, target):
            low, high = 0, len(nums) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    res = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        
        def right(nums, target):
            low, high = 0, len(nums) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    res = mid
                    low = mid + 1 
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        
        le = left(nums, target)
        if le == -1:
            return [-1, -1]
        ri = right(nums, target)
        return [le, ri] 