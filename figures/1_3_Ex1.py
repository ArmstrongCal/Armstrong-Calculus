from figures import *
from defaults import *

width = standardwidth*0.8
height = standardheight*1.2
beginfigure("1_3_Ex1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -6, 3, 1])

grid = Grid([-1, 1, 3], [-6, 1, 1])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-5, 1, 0])
axes.drawticks()

axes.setlabels([1, 1, 2], [-4, 2, 1])
axes.drawlabels()


label = Label(r"$y=x-x^2$", [0.8, -5.8])
label.draw()

label = Label(r"$m = f'(2)$", [1.3, 0.4])
label.draw()


def f(x):
    return x-x*x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

a = 2
dx = 1
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([2,f(2)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

endfigure()
