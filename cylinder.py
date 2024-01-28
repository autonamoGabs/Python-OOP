import math

class Cylinder:
    pu = math.pi
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        print(self.pu*self.radius**2 * self.height)
    
    def surface_area(self):
        print(2 * self.pu * self.radius**2  + 2 * self.pu * self.radius * self.height)
# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()
