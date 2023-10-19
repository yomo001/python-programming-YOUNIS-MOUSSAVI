import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle, Rectangle as pltRectangle
import math

# In this module you will find
# 1. Class GeometricShapes
# 2. Class Circle (Inheriting from GeometricShapes)
# 3. Class Rectangle (Inheriting from GeometricShapes)
# 4. Class Cube (Inheriting from Rectangle)
# 5. Class Sphere (Inheriting from Circle)
# 6. Main function for assessment statements from labb3 instructions


# 1. Class GeometricShapes

class GeometricShapes:          
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):                # OBS BEHÖVER EJ HA PROPERTY OCH SETTER OM MAN ÄNDÅ SKA ÄNDRA DIREKT. BARA OM MAN INTE SKULLE ÄNDRA ALLS:
        return self._x           # OBS SE ÖVER SÅ ATT MAN SKA KUNNA SÄTTA DET TILL ANNAT I EFTERHAND

    @x.setter
    def x(self, new_x):          # OBS SE ÖVER SÅ ATT MAN SKA KUNNA SÄTTA DET TILL ANNAT I EFTERHAND
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y
    
    @property                                   # Area property
    def area(self):
        return "This is meant to be overridden"

    def translate(self, new_x, new_y):         # Method for translating the shape
            try:
                self.x = float(new_x)
                self.y = float(new_y)
            except ValueError:
                error_alert = f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics."
                print(error_alert)            # Because assessment question in labb3 required printing it out when entering it.
                return error_alert
            
    def __eq__(self, other):                   # Operator overload of ==
        return type(self) is type(other)       # OBS - ÄNDRA HÄR, TILL AREA
 
    def __lt__(self, other):                   # Operator overload of <
        return self.area < other.area

    def __le__(self, other):                   # Operator overload of <=
        return self.area <= other.area

    def __gt__(self, other):                   # Operator overload of >
        return self.area > other.area

    def __ge__(self, other):                   # Operator overload of >=
        return self.area >= other.area




# 2. Class Circle (Inheriting from GeometricShapes)

class Circle(GeometricShapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        try:                                    # ONÖDIGT, TA BORT TRY METODEN
            self._radius = float(radius)        # Specifik for circle, added to __init__ inheritance from superclass
        except ValueError as e:
            print(f"{e}")

    @property                                   # Area property
    def area(self):
        return math.pi * self._radius**2

    @property                                   # Circumference property
    def circumference(self):
        return 2 * math.pi * self._radius

    def __repr__(self):                         # __repr__ override 
                                                # ÄNDRA SKRIV UT PYTHONKOD SOM GÖR INSTANSKOD FÖR LIKADAN CIRKEL
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def __str__(self):                          # __str__ override
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def is_unit_circle(self):                   # Method for assessing if circle is a unit circle
        return self._x == 0 and self._y == 0 and self._radius == 1

    def is_inside(self, x, y):        # Method for assessing if a point is within the circle
        # OBS EJ BIEFFEKT TA BORT PLOTTEN self.plot(x, y)               # Plot to visualize the point in relation to the circle
        distance = math.sqrt((x-self._x)**2+(y-self._y)**2)
        return distance <= self._radius

    def plot(self, x = None, y = None):    # TA BORT X, Y ,      Method for plotting the circle
        # The figure and graphics
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if x is not None and y is not None:      # TA BORT X och Y
            plt.plot(x, y, 'ro')

        # The plot
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        plt.show()



    
# 3. Class Rectangle (Inheriting from GeometricShapes)

class Rectangle(GeometricShapes):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        try:   
            self._width = float(width)                      # Specifik for rectangle, added to __init__ inheritance from superclass
            self._height = float(height)                    # Specifik for rectangle, added to __init__ inheritance from superclass
        except ValueError as e:
            return f"{e}"

    @property                                               # Area property
    def area(self):
        return self._width * self._height
    
    @property                                               # Circumference property
    def circumference(self):
        return 2*(self._width + self._height)

    def __repr__(self):                                     # __repr__ override
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"

    def __str__(self):                                      # __str__ override
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"
              
    def is_square(self):                                    # Method to check if shape is a square
        return self._width == self._height
    
    def is_inside(self, test_x, test_y):   #ÄNDRA TILL X OCH Y                 # Method for assessing if a point is within the rectangle
        self.plot(test_x, test_y)                           # Plot to visualize the point in relation to the rectangle
        distance_x = abs(test_x-self._x) # OBS ÄNDRAT , så att det funkar för - värden, lägg till i testet, värden utanför och innanför kvadraten, positiva och negativa
        distance_y = abs(test_y-self._y)
        return distance_x <= self._width/2 and distance_y <= self._height/2      # Distance from x/y min, max for assessment
        
    def plot(self, test_x = None, test_y = None):          # Method for plotting the rectangle
        # The figure and graphics
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')

        # The plot
        x_min = self._x - self._width/2
        y_min = self._y - self._height/2
        rectangle = pltRectangle((x_min, y_min), self._width, self._height, fill = False)
        ax.add_patch(rectangle)
        plt.show()




# 4. Class Cube (Inheriting from Rectangle) # OBS ÄRV FRÅN GEOMETRIC SHAPES, OLOGISKT ANNARS.
# SUPER CLASS SOM HETER SHAPE, SEDAN FRÅN DEN SHAPE 2 D och SHAPE 3 D. och sedan 3 D ÄRVER DET DOM SKA HA. LOGISKEN STÄMMER BÄTTRE DÅ
# Plotten räcker för de två första. 
# Is_inside plotta separat, via main

class Cube(Rectangle):
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, width, height)
        try:   
            self._z = z                     # Specifik for cube, added to __init__ inheritance from superclass
            self._depth = float(depth)      # Specifik for cube, added to __init__ inheritance from superclass
        except ValueError as e:
            return f"{e}"

    @property                               # Area property
    def area(self):
        return 2*self._width**2 + 2*self._height**2 + 2*self._depth**2      # area of all sides added 
    
    @property                               # Circumference property
    def circumference(self):
        return 4* self._width              # HA MED VOLYM # ÄNDRA OMKRETS PÅ 3D BEHÖVS EJ, 3D SHAPES HAR INTE OMKRETS, BEROENDE PÅ HUR MAN MÄTER  # If it is a cube, then width, height and depth are the same, so 4 x optional side

    @property                              # Property for z coordinate
    def z(self):
        return self._z

    @z.setter
    def z(self, new_z):
        self._z = new_z

    def __repr__(self):                     # __repr__ overload
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"

    def __str__(self):                      # __str__ overload
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"
              
    def is_cube(self):                      # Method for assessing if the shape is a cube
        return self._width == self._height == self._depth

    def is_inside(self, test_x, test_y, test_z):         # Method for assessing if a point is within the cube. Polymorphism.                               
        self.plot(test_x, test_y)                        # Plotting the point to visualize its relation to the cube (obs 2D, depth not visualized)
        distance_x = test_x-self._x    #ÄNDRA O VÄLJ ABSOLUTA VÄRDET                  # Assessing distance from x,y,z min, max 
        distance_y = test_y-self._y
        distance_z = test_z-self._z
        return distance_x <= self._width/2 and distance_y <= self._height/2 and distance_z <= self._depth/2

    def translate(self, new_x, new_y, new_z):           # Translate method. Polymorphism.
        try:
            self.x = float(new_x)   ### ÄNDRA ; x första + x förflyttning
            self.y = float(new_y)   ## ÄNDRA BEHÖVER EJ KONVERTERA TILL FLOATS, FÖRUTSÄTTER ATT DET ÄR DET VI SKICKAR IN
            self.z = float(new_z)
        except ValueError:
            error_alert = f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', all have to be numerics."
            print(error_alert)
            return(error_alert)




# 5. Class Sphere (Inheriting from Circle)

class Sphere(Circle):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius)
        try:   
            self._z = float(z)                      # Specifik for sphere, added to __init__ inheritance from superclass
        except ValueError as e:
            return f"{e}"

    @property                                       # Area property
    def area(self):
        return math.pi*4*self._radius**2

    @property                                       # Circumference property
    def circumference(self):
        return 2 * math.pi * self._radius
    
    @property                                       # Property for z coordinate
    def z_coordinate(self):
        return self._z

    @z_coordinate.setter
    def z_coordinate(self, new_z):
        self._z = new_z

    def __repr__(self):                             # __repr__ overload
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def __str__(self):                              # __str__ overload
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def is_unit_sphere(self):                       # Method for checking if sphere is a unit sphere
        return self._x == 0 and self._y == 0 and self._z == 0 and self._radius == 1

    def is_inside(self, test_x, test_y, test_z):    # Method for checking if point is within sphere
        self.plot(test_x, test_y)                   # Plot to visualize point in relation to square (obs, 2D, depth not visualized)
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2+(test_z-self._z)**2)   # excercise 0 och https://stackoverflow.com/questions/26818772/python-checking-if-a-point-is-in-sphere-with-center-x-y-z
        return distance <= self._radius              
        
    def translate(self, new_x, new_y, new_z):       # Polymorphism of translate method
        try:
            self.x = float(new_x)
            self.y = float(new_y)
            self.z_coordinate = float(new_z)
        except ValueError:
            error_alert = f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', all have to be numerics."
            print(error_alert)
            return error_alert
    





# 6. Main function for assessment statements from labb3 instructions
# Main ska ligga som en egen. 
def main():
    
    # Controls from labb3 assignment instructions. All passed.
    cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
    cirkel2 = Circle(x=1,y=1, radius=1)
    rektangel = Rectangle(x=0,y=0,width=1, height=1)
    print(cirkel1==cirkel2) # True
    print(cirkel2==rektangel) # False
    print(cirkel1.is_inside(0.5, 0.5)) # True
    cirkel1.translate(5,5)
    print(cirkel1.is_inside(0.5, 0.5)) # False
    cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar

if __name__ == "__main__":               # To avoid "loose code" from running when importing module
    main()

