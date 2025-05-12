class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def grr(i):
            a = []
            while i != 0:
                a.append(i % 10)
                i //= 10
            return a

        m = []
        for i in range(100, 1000):
            if i % 2 != 0:
                continue
            g = grr(i)
            temp = list(digits)  # don't mess original
            ok = True
            for digit in g:
                if digit in temp:
                    temp.remove(digit)
                else:
                    ok = False
                    break
            if ok:
                m.append(i)
        return sorted(m)
