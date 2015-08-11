from figures import *
from defaults import*

width = 180
height = 120
beginfigure("1_4_Ez3b", 2*width, 2*height)

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
    return (x+4)**2 - 3

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-6,-3])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return 2*(x+3)-2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-3,0])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return (x-2)**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([0,3])
graph.setcolor(graphcolor)
graph.draw()

def f(x):
    return 0.5*(x-3)+1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([3,6])
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
    return 2*math.cos(pi*x/2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

label = Label(r"$f$", [0.2,3.2], alignment = "lb", offset = [2, 2] )
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
