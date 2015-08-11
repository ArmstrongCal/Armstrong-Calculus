from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_6_Intro2", width, height)

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

axes.sethticks([-2, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 1, 2])
axes.drawticks()

axes.setlabels([-2, 2, 2], [-2, 2, 2])
axes.drawlabels()


def f(x):
    return 2*math.cos(0.5*pi*x) + 0.5

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3,3])
graph.draw()

a = 0.2
dx = 0.8
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([0.2,f(0.2)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$A$", [0.2,f(0.2)], alignment = "lb", offset = [4, 4])
label.draw()

a = 2.2
dx = 0.7
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

label = Label(r"$B$", [2.2,f(2.2)], alignment = "lt", offset = [4, -4])
label.draw()

label = Label(r"$y=f(x)$", [-1.8,f(-1.8)], alignment = "ct", offset = [0, -2])
label.draw()

restore()

endfigure()
