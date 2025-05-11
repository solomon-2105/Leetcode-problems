class Solution:
    def isPalindrome(self, s):
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch.lower()
        
        n = len(res)
        return self.checkPalindrome(0, res, n)

    def checkPalindrome(self, i, res, n):
        if i >= n // 2:
            return True
        if res[i] != res[n - i - 1]:
            return False
        return self.checkPalindrome(i + 1, res, n)
