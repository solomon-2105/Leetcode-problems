class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        result = n
        a = [0 , 0]
        for i in range(n):
            a[( ord( s[i] ) ^ i ) & 1] += 1
        for i in range(n):
            b = ord(s[i])
            a[( b ^ i ) & 1] -= 1
            a[(b ^ (n + i)) & 1] += 1
            result = min(result , min(a))
        return result