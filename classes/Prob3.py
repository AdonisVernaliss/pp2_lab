class Square:
    def __init__(self, length=0):
        self.length = length

    def area(self):
        print(self.length*self.length)


class Shape(Square):
    def __init__(self, length=0):
        super().__init__(length)
    def area(self):
        print(self.length*self.length)
    # def area(self):
    #     super().area()
    

class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)

# sq = Shape(5)
rt = Rectangle(5,9)
rt.area()