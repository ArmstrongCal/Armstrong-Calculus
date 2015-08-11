from figures import *
from defaults import *

width = 120
height = 120

beginfigure("1_3_SecToTanSeq", 4*width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.8, -0.7])
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
graph.setdomain([0.2,3.3])
graph.draw()

point = Point([2.5, f(2.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 2

save()

margin = 5
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.8, -0.7])
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
    return f(1) + (f(2)-f(1))/(2-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,2.8])
graph.draw()

point = Point([2, f(2)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 3

save()

margin = 5
setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.8, -0.7])
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
    return f(1) + (f(1.5)-f(1))/(1.5-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,2.3])
graph.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 4

save()

margin = 5
setupcoordinates([3*width+margin, margin, 4*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)

label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.8, -0.7])
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 1
dx = 1.2
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

restore()

endfigure()
