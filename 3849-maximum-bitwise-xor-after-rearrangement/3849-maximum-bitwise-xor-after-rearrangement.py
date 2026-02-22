class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        o = 0
        for i in t:
            if i == '1': o += 1
        z = len(t) - o
        res = []
        for i in s:
            if i == '0':
                if o > 0:
                    res.append('1')
                    o -= 1
                else:
                    res.append('0')
                    z -= 1
            else:
                if z > 0:
                    res.append('1')
                    z -= 1
                else:
                    res.append('0')
                    o -= 1
        return "".join(res)