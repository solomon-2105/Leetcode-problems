class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.merge_sort(nums, 0, len(nums)-1)
        return nums

    def merge_sort(self, nums, l, h):
        if l >= h:
            return
        m = (l + h) // 2
        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m+1, h)
        self.combine(nums, l, m, h)

    def combine(self, nums, l, m, h):
        lx = m - l + 1
        ly = h - m

        left = [0] * lx
        right = [0] * ly

        for i in range(lx):
            left[i] = nums[l + i]
        for i in range(ly):
            right[i] = nums[m + 1 + i]

        i = j = 0
        k = l

        while i < lx and j < ly:
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < lx:
            nums[k] = left[i]
            i += 1
            k += 1

        while j < ly:
            nums[k] = right[j]
            j += 1
            k += 1
