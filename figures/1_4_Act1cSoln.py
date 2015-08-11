from figures import *
from defaults import*

width = 180
height = 120
beginfigure("1_4_Act1cSoln", 2*width, 2*height)

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
    return x + 2/pi*math.sin(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

label = Label(r"$r$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
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
    return x + 2/pi*math.sin(pi*x/2)

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.draw()

label = Label(r"$r'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2] )
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
    return -x-3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-6,0])
graph.draw()

def f(x):
    return x-3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([0,6])
graph.draw()

label = Label(r"$s$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

## grid for second function's derivative

save()
margin = 5
setupcoordinates([width+2*margin,margin,2*width-margin,height-margin], 
                 [-6, -4, 6, 4])

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return -x-3

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([-6,0])
graph.draw()

def f(x):
    return x-3

derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setdomain([0,6])
graph.draw()

p1 = Point([0,-1], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([0,1], 1.3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

label = Label(r"$s'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
