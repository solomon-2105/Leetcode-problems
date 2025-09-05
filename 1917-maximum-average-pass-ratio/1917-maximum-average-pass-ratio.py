class Solution:
    def maxAverageRatio(self, cl: List[List[int]], ex: int) -> float:
        # a=[]
        # while ex:
        #     maxi=float('-inf')
        #     brr=[]
        #     for i in range(len(cl)):
        #         brr.append(cl[i][0]/cl[i][1])
        #     crr=[]
        #     for i in range(len(cl)):
        #         crr.append((cl[i][0]+1)/(cl[i][1]+1))
        #     h=0
        #     for i in range(len(cl)):
        #         if maxi<(crr[i]-brr[i]):
        #             maxi=crr[i]-brr[i]
        #             h=i
        #     cl[h][0]+=1
        #     cl[h][1]+=1
        #     ex-=1
        # for i in range(len(cl)):
        #     a.append(cl[i][0]/cl[i][1])
        # return round(sum(a)/len(a),5)
        a=[]
        hq=[]
        for i in range(len(cl)):
            p,t=cl[i]
            d=(p+1)/(t+1)-p/t
            heapq.heappush(hq,(-d,i))
        while ex:
            d,i=heapq.heappop(hq)
            cl[i][0]+=1
            cl[i][1]+=1
            p,t=cl[i]
            nd=(p+1)/(t+1)-p/t
            heapq.heappush(hq,(-nd,i))
            ex-=1
        for i in range(len(cl)):
            a.append(cl[i][0]/cl[i][1])
        return round(sum(a)/len(a),5)


