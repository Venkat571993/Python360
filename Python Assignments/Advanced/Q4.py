class Shape:
    def __init__(self,len=0):
        self.length =len
        self.fn_area()

    def fn_area(self):
        area = self.length*self.length
        print(area)


class Square(Shape):
    def __init__(self, len):
        super().__init__(len)


shape1 = Shape()

square1 = Square(5)








        
