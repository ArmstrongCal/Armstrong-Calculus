from figures import *
from defaults import*

width = 180
height = 120
beginfigure("1_4_Ez3a", 2*width, 2*height)

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
    return -2*(x+3)-3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-6,-3])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return -3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-3,-1])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return -3 + 1*(x+1)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-1,1])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return -1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([1,2])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return -1+2*(x-2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([2,3])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return 1-2*(x-3)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([3,5])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return -3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([5,6])
graph.setcolor(graphcolor)
graph.draw()

label = Label(r"$f$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
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

label = Label(r"$f'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
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
    return 3*math.exp(-0.2*x*x)+1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([-6,6])
graph.draw()

label = Label(r"$f$", [0.2,2.8], alignment = "lb", offset = [2, 2] )
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

label = Label(r"$f'$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$x$", [5.2,0.2], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
