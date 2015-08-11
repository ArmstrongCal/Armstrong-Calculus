from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_5_Ex1", 2*width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 4, 4])

grid = Grid([-1, 0.5, 4], [-1, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 3])
axes.setvticks([0, 1, 3])
axes.drawticks()
axes.sethticksize(10)

axes.setlabels([0, 1, 3], [0, 1, 3])
axes.drawlabels()


def f(x):
    return 4 - 3*2**(-x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,4])
graph.draw()

def g(x):
    return f(1) + (f(2)-f(1))/(2-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(gray)
graph.setlinewidth(graphwidth)
graph.setdomain([0.4,2.6])
graph.draw()

def g(x):
    return f(3) + (f(3)-f(2))/(3-2)*(x-3)

graph = Graph(Function(g))
graph.setcolor(gray)
graph.setlinewidth(graphwidth)
graph.setdomain([1.4,3.6])
graph.draw()

a = 2
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()



p1 = Point([1,f(1)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([2,f(2)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([3,f(3)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

####

save()
margin = 5
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1, -1, 4, 4])

grid = Grid([-1, 0.5, 4], [-1, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 3])
axes.setvticks([0, 1, 3])
axes.drawticks()
axes.sethticksize(10)

axes.setlabels([0, 1, 3], [0, 1, 3])
axes.drawlabels()



def f(x):
    return 4 - 3*2**(-x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,4])
graph.draw()

a = 2
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

def g(x):
    return f(1) + (f(3)-f(1))/(3-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(red)
graph.setlinewidth(graphwidth)
graph.setdomain([0.4,3.6])
graph.draw()

p1 = Point([1,f(1)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([2,f(2)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([3,f(3)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

endfigure()
