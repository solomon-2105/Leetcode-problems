class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        summ = 0
        b=[]
        for i in range( len(nums) ) :
            b.clear()
            c = self.divisors( nums[i] ,b)
            if len(c) == 4 :
                summ += sum(c)
        return summ

    def divisors(self, a, b):
        for i in range( 1, int( a ** 0.5 ) + 1 ) :
            if a % i == 0 :
                b.append(i)
                if ( a // i ) != i :
                    b.append( a // i )
        return b