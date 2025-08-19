class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t=0,0
        for i in bills:
            if i==5: f+=1
            elif i==10:
                if not f: return False
                f-=1
                t+=1
            else:
                if f>0 and t>0:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else : return False
        return True