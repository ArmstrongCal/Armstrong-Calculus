from figures import *
from defaults import*

width = 180
height = 120
beginfigure("1_6_Act2Soln", 2*width, 3*height)

save()
margin = 5
setupcoordinates([margin,2*height+margin,width-margin,3*height-margin], 
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
    return -0.03*(x-5)*x*(x+4)-1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

label = Label(r"$f$", [0.2,3.2], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

### grid for first derivative

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

def f(x):
    return -0.03*(x-5)*x*(x+4)-1
derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.draw()

label = Label(r"$f'$", [0.2,3.2], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

### grid for second derivative

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
    return -0.03*(x-5)*x*(x+4)-1
derivative = Function(f).differentiate()
secondderivative = derivative.differentiate()
graph = Graph(secondderivative, color=red)
graph.draw()

label = Label(r"$f''$", [0.2,3.2], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

############## second original function graph

save()
margin = 5
setupcoordinates([width+2*margin,2*height+margin,2*width-margin,3*height-margin], 
                 [-6, -4, 6, 4])

xrange = [-6, 1, 6]
yrange = [-4, 1, 4]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2*math.exp(-0.2*(x**2))*(1+math.cos(x**2))-1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

label = Label(r"$f$", [0.2,3.2], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

## grid for second function's derivative

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
    return 2*math.exp(-0.2*(x**2))*(1+math.cos(x**2))-1
derivative = Function(f).differentiate()
graph = Graph(derivative, color=green)
graph.setN(2000)
graph.draw()

label = Label(r"$f'$", [0.2,3.2], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

## grid for second function's second derivative

save()
margin = 5
setupcoordinates([width+2*margin,margin,2*width-margin,height-margin], 
                 [-6, -12, 6, 12])

xrange = [-6, 1, 6]
yrange = [-12, 3, 12]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2*math.exp(-0.2*(x**2))*(1+math.cos(x**2))-1

derivative = Function(f).differentiate()
secondderivative = derivative.differentiate()
graph = Graph(secondderivative, color=red)
graph.setN(2000)
graph.draw()

label = Label(r"$f''$", [0.2,9.6], alignment = "lb", offset = [2, 2], scale=0.8)
label.draw()

label = Label(r"$x$", [5.2,-0.2], alignment = "lt", offset = [2, -2], scale=0.8)
label.draw()

restore()

endfigure()
