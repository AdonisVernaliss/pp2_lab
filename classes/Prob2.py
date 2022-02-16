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
    


sq = Shape(5)
sq.area()