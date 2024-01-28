class Line:
    
    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        print(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)
    
    def slope(self):
        print((self.y2 - self.y1) / (self.x2 - self.x1))
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()

li.slope()
