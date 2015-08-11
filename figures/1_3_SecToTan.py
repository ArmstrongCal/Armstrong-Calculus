from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_3_SecToTan", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.2])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.9, -0.5])
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(2.5)-f(1))/(2.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,4.3])
graph.draw()

def g(x):
    return f(1) + (f(2.0)-f(1))/(2.0-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.0,3.7])
graph.draw()

def g(x):
    return f(1) + (f(1.5)-f(1))/(1.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.2,2.9])
graph.draw()

a = 1
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2.5, f(2.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([2.0, f(2.0)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

box = Box([0.3, f(1)-0.7, 1.4, 1.4], color = gridcolor)
box.draw()

restore()
save()

## now for the adjacent figure

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [0.3,0.7,1.7,2.1])

outline = Box([0.3,0.7,1.4,1.4], color=gridcolor) # arguments are lower left corner, width and heigh
outline.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
##graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(1.5)-f(1))/(1.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
##graph.setdomain([-0.2,2.9])
graph.draw()

a = 1
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
##tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

restore()


endfigure()
