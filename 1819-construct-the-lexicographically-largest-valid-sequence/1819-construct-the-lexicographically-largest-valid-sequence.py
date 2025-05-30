class Solution(object):
    def constructDistancedSequence(self,n):
        result=[0]*(2*n-1)
        used=[False]*(n+1)
        self.backtrack(result,used,0,n)
        return result

    def backtrack(self,result,used,index,n):
        if index==len(result):return True
        if result[index]!=0:return self.backtrack(result,used,index+1,n)
        for num in range(n,0,-1):
            if used[num]:continue
            if num==1:
                result[index]=1
                used[1]=True
                if self.backtrack(result,used,index+1,n):return True
                result[index]=0
                used[1]=False
            else:
                nextIndex=index+num
                if nextIndex<len(result) and result[nextIndex]==0:
                    result[index]=result[nextIndex]=num
                    used[num]=True
                    if self.backtrack(result,used,index+1,n):return True
                    result[index]=result[nextIndex]=0
                    used[num]=False
        return False