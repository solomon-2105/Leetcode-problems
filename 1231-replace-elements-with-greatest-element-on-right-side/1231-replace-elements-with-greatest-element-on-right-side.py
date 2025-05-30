class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        result = [0] * n
        result[n-1] = -1
        max_val = -1

        i = n - 2
        while i >= 0:
            max_val = max(max_val, arr[i+1])
            result[i] = max_val
            i -= 1

        return result
