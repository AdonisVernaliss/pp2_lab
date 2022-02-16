from math import sqrt

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def show(self):
        print(self.x,self.y)

    def move(self, a, b):
        self.x = a
        self.y = b

    def dist(self, p):
        d = sqrt((self.x-p.x)**2+(self.y-p.y)**2)
        print(d)

p1 = Point(7,5) 
p2 = Point(4,2)

p1.show()
p1.move(4,3)
p1.show()
p1.dist(p2)

# print (p1.x)


# class A{
#     int x, y;

#     A(int coord1, coord2){
#         x= coord1;
#         y= coord2;
#     }
# }

# int main(){
#     A p = A(7,5);
#     p.x
#     p.y 
# }