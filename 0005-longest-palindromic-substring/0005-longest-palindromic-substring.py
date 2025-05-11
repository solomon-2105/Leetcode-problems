class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_len = 1

        def expand(l: int, r: int):
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)       # Odd-length palindrome
            expand(i, i + 1)   # Even-length palindrome

        return s[start:start + max_len]