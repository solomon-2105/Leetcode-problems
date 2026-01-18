class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c , v = 0 , 0
        for i in s:
            if i in 'aeiou':
                v += 1
            elif i.isalpha() and i not in 'aeiou':
                c += 1
        if c > 0:
            return v//c
        return 0