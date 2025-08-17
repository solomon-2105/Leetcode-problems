class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        res = ""
        for i in range(len(a[0])):
            char = a[0][i]
            for j in range(1, len(a)):
                if i >= len(a[j]) or a[j][i] != char:
                    return res
            res += char
        return res