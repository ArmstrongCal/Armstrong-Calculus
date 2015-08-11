from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_6_Intro", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -3, 3, 3])

grid = Grid([-3, 1, 3], [-3, 1, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return x-0.25*x**3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3,3])
graph.draw()

a = -0.8
dx = 1.2
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([-0.8,f(-0.8)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$A$", [-0.8,f(-0.8)], alignment = "rb", offset = [-4, 4])
label.draw()

a = 2.2
dx = 0.6
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([2.2,f(2.2)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$B$", [2.2,f(2.2)], alignment = "rt", offset = [-4, -4])
label.draw()

restore()

endfigure()
