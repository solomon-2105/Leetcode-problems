class Solution:
    def countMonobit(self, n: int) -> int:
        # if n == 0 : return 1
        # if n == 1: return 2
        # count = 2
        # for i in range(3,n+1):
        #     a = [0,0]
        #     j = i
        #     while j:
        #         if j % 2 == 0: a[0] = 1
        #         else : a[1] = 1
        #         j //= 2
        #     if a[0] != a[1]:
        #         count += 1
        # return count

        count = 1
        k = 1
        while (1 << k) - 1 <= n:
            count += 1
            k += 1
        return count  