class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for n in range(left, right + 1):
            m = n
            ok = True
            while m:
                d = m % 10
                if d == 0 or n % d:
                    ok = False
                    break
                m //= 10
            if ok:
                res.append(n)
        return res