class Combinations:
    def __init__(self, n , r):
        self.arr = [1] * int(r)
            self.init_value = -1
                self.i = -1
                self.recursion_count = 0
        
        def generate_combinations(self, n, r):
            self.i = self.i + 1
                
                if r == 0:
                    print ( self.arr )
                else:
                    if self.i != 0:
                        self.init_value = self.arr[self.i-1]
                        
                        self.arr[self.i] = self.init_value + 1
                        while self.arr[self.i] < int(n):
                            self.generate_combinations(n, r - 1)
                                self.arr[self.i] = self.arr[self.i] + 1
                
            self.i = self.i - 1

n = int(input())
r = int(input())
generator = Combinations(n, r)
generator.generate_combinations(n, r)
