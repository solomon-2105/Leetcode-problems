class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # Calculate left products and store in result
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Calculate right products and multiply with the left products in result
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result