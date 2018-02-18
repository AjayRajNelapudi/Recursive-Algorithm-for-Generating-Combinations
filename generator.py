class generate_combinations:
    def __init__(self,a):
        self.arr=a
        self.i=-1
        self.init=0

    def generate(self,n,r):
        self.i=self.i+1
        if r == 0:
            print (self.arr)
        else:
            if self.i!=0:
                self.init=self.init+1
            for i in range(self.init,n):
                self.generate(self,n,r-1)

c=generate_combinations
c.generate(c,10,5)