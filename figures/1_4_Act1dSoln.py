from figures import *
from defaults import*

width = 180
height = 120
beginfigure("1_4_Act1dSoln", 2*width, 2*height)

save()
margin = 5
setupcoordinates([margin,height+margin,width-margin,2*height-margin], 
                 [-6, -4, 6, 4])

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

### first original function graph

def f(x):
    return math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-4,-2])
graph.draw()

def f(x):
    return math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([0,2])
graph.draw()

def f(x):
    return math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([4,6])
graph.draw()

def f(x):
    return -math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-6,-4])
graph.draw()

def f(x):
    return -math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-2,0])
graph.draw()

def f(x):
    return -math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([2,4])
graph.draw()

label = Label(r"$w$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2] )
label.draw()

restore()

### grid for first derivative

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-6, -4, 6, 4])

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return math.sin(pi*x/2)

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([-4,-2])
graph.draw()

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([0,2])
graph.draw()

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([4,6])
graph.draw()

def f(x):
    return -math.sin(pi*x/2)

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([-6,-4])
graph.draw()

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([-2,0])
graph.draw()

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([2,4])
graph.draw()

p1 = Point([-4,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-4,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-2,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-2,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([0,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([0,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([2,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([2,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([4,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([4,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-6,1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([6,-1.57], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

label = Label(r"$w'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

############## second original function graph

save()
margin = 5
setupcoordinates([width+2*margin,height+margin,2*width-margin,2*height-margin], 
                 [-6, -4, 6, 4])

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2/x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-6.2,-0.1])
graph.draw()

def f(x):
    return 2/x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([0.1,6])
graph.draw()

label = Label(r"$z$", [-0.2,3.2], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2] )
label.draw()

restore()

## grid for second function's derivative

save()
margin = 5
setupcoordinates([width+2*margin,margin,2*width-margin,height-margin], 
                 [-6, -4, 6, 4])

cliptoboundingbox() 

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2/x

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([-6.2,-0.5])
graph.draw()


def f(x):
    return 2/x

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([0.5,6])
graph.draw()

label = Label(r"$z'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
