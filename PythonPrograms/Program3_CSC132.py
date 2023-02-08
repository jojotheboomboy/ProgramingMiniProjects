######################################################################################################################
# Name: Josiah Norman
# Date: 3/22/2021
# Description: This program will create a window using tkinter that is equal (in size) to the parameter's HEIGHT and WEIGHT
# It will then print an oval at some random coordinate "NUM_POINTS" amount of times. The oval's color will be chosen using a list
# of colors and "choice" from the library random. the size of each oval will be dictated according to the paremeter "radius"'s value.
######################################################################################################################
from tkinter import *
from random import choice 
from random import randint

# the 2D point class
class Point:
    
    # sets x and y values to default at 0.
        def __init__ (self, x = 0, y = 0):
            self.x = x
            self.y = y

        # Accesor for x
        @property
        def x (self):
            return self._x

        # Mutator for x
        @x.setter
        def x (self, value):
            self._x = float(value)

        # Accesor for y
        @property
        def y (self):
            return self._y

        # Mutator for y
        @y.setter
        def y (self, value):
            self._y = float(value)

        # Returns a touple of x and y
        def GetPoint (self):
            return self.x, self.y

        # Print statement        
        def __str__ (self):
            return "({}, {})".format(self.x,self.y)

        # Programmed version of the distance equation
        def dist (self, plot):
            total_x = (self.x - plot.x)
            final_x = (total_x * total_x)
            total_y = (self.y - plot.y)
            final_y = (total_y * total_y)
            distance = math.sqrt(final_x + final_y)
            return distance

        # Programmed version of the midpoint equation
        def midpt (self, plot):
            mid_x = (self.x + plot.x)/2
            mid_y = (self.y + plot.y)/2
            return Point(mid_x, mid_y)

# Inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
        # Class variables:
        # List of colors
        colors = ["red", "green", "blue", "cyan", "yellow", "magenta"]
        # Radius which can be customized by simply changing the integer value which it is assigned to.
        radius = 6

        list = []
        
        # This constructer updates each time a cordinate is added to the GUI
        def __init__(self, window):
                Canvas.__init__(self, window, bg = "white")
                self.pack(fill = BOTH, expand = 1) 
                
        # This code will plot a point an equivilent amount of times to that of the numerical value that is associated with "NUM_POINTS"
        def plotPoints(self):
                    #create a random point within the limits
                    p = Point(MIN_X, MAX_Y)
                    q = Point(MAX_X, MAX_Y)
                    r = Point(MID_X, MIN_Y)
                    #call the plot function on that point...
                    self.plot(p)
                    self.plot(q)
                    self.plot(r)
                    

        def plotMidPoints(self, NUM_POINTS):
                p = Point(MIN_X, MAX_Y)
                q = Point(MAX_X, MAX_Y)
                r = Point(MID_X, MIN_Y)
                vertex = [p, q, r]
                last = p.midpt(q)
                for i in range(NUM_POINTS):
                    
                    #create a random point within the limits
                    last = last.midpt(choice(vertex))
                    self.plot2(last)
                    
                    
            
                        
        #use a separate plot function and use the create_oval function 
        def plot(self, p):
                self.create_oval(p.x - self.radius/2, p.y - self.radius/2, p.x + self.radius/2, p.y + self.radius/2, fill=choice(CoordinateSystem.colors))

        def plot2(self, p):
            self.create_oval(p.x, p.y, p.x + 1, p.y + 1)
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***

# the default size of the canvas is 800x800
WIDTH = 600
HEIGHT = 520

MIN_X = 10
MAX_X = 590
MID_X = ((MIN_X + MAX_X)/2)

MIN_Y = 10
MAX_Y = 510
MID_Y = ((MIN_Y + MAX_Y)/2)


# the number of points to plot
NUM_POINTS = 50000

# create the window
window = Tk()
                        
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")

# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)

# plot some random points
s.plotMidPoints(NUM_POINTS)
s.plotPoints()


# wait for the window to close
window.mainloop()
