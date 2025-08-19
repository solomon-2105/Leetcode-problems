class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        a={} #ball and color
        col_count={} #color and frequencies
        brr=[] #final array to return the distinct colors after ith query anta
        for ball,color in queries:
            if ball in a:
                old_color=a[ball]
                if old_color!=color:
                    col_count[old_color]-=1
                    if col_count[old_color]==0:
                        del col_count[old_color]
                    a[ball]=color
                    if color in col_count:
                        col_count[color]+=1
                    else:
                        col_count[color]=1
            else:
                a[ball]=color
                if color in col_count:
                    col_count[color]+=1
                else:
                    col_count[color]=1
            brr.append(len(col_count))
        return brr
