class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        sum = cnt = 0
        node_left = float('inf')
        for n in nums:
            x = n ^ k
            sum += max(n, x)
            cnt += x > n
            node_left = min(node_left, abs(n - x))
        return sum - (node_left if cnt & 1 else 0)