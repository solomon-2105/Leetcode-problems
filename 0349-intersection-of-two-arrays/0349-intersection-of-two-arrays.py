class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create a hash set to store unique elements of nums1
        nums1_set = {}
        for num in nums1:
            nums1_set[num] = True

        # List to store the intersection result
        result = []

        # Iterate over nums2 and check for common elements
        for num in nums2:
            if num in nums1_set:
                result.append(num)
                del nums1_set[num]  # Avoid duplicates in the result

        return result
