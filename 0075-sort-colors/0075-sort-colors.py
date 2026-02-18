class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # (0) 00000000000(low-1) 
        # (low) 111111111111111 (mid-1) 
        # (mid) 2 0 2 1 1 0 (high)
        # (high+1) 2222222222222222 (len(a)-1)

        low , mid , high = 0 , 0 , len(nums)-1
        while mid <= high :
            if nums[mid] == 0:
                nums[mid] , nums[low] = nums[low] , nums[mid]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1