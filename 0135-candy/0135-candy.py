class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        count=0
        sinai=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                sinai[i]=sinai[i-1]+1
        for i in range(n-1,0,-1):
            if ratings[i-1]>ratings[i]:
                sinai[i-1]=max(sinai[i]+1,sinai[i-1])
            count+=sinai[i-1]
        return count+sinai[n-1]