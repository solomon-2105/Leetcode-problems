class Solution:
    def minOperations(self, n: List[int]) -> int:
        if len(set(n))==1: return 0
        else: return 1