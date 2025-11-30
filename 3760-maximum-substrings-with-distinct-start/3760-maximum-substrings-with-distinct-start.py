class Solution:
    def maxDistinct(self, s: str) -> int:
        # a=set()
        # for i in range(len(s)):
        #     if s[i:][0] in a:
        #         continue
        #     else:
        #         a.add[s[i:]]
        # return len(a)
        a=set(s)
        return len(a)