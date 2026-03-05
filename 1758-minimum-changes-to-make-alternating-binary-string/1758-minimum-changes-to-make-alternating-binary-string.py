class Solution:
    def minOperations(self, s: str) -> int:
        start_with_zero = start_with_one = 0
        for i in range(len(s)):
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                start_with_zero += 1
        for i in range(len(s)):
            if (i % 2 == 0 and s[i] == '0') or (i % 2 == 1 and s[i] == '1'):
                start_with_one += 1
        return min(start_with_zero , start_with_one)