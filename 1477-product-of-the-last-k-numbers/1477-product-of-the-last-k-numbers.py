class ProductOfNumbers:

    def __init__(self):
        
        self.pre=[1]
        self.count=1
    
    

    def add(self, num: int) -> None:
        if num:
        
            self.pre.append(self.pre[-1]*num)
           
            self.count+=1    
        else:
            self.count=1
            self.pre=[1]


        
    def getProduct(self, k: int) -> int:
        # print(self.pre)
        if k>=self.count:
            return 0
        else:
            return self.pre[-1]//self.pre[self.count-k-1]    