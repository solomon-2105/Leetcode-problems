class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        se = ('a' , 'e' , 'i', 'o' , 'u')
        res = list(s)
        for i in range(len(s)-1 , -1 , -1):
            if s[i] in se:
                res.pop()
            else:
                break
        return "".join(res)