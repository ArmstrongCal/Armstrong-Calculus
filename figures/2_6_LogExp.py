from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_6_LogExp", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 10, 10])

grid = Grid([-5, 1, 10], [-5, 1, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 2, 8]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 8])
axes.drawticks()

axes.setlabels([-4, 4, 8], # you can do this separately with seth(v)labels
               [-4, 4, 8])
axes.drawlabels()

label = Label(r"$y = e^x$", [2.5, 8.5])
label.draw()

label = Label(r"$y = \ln(x)$", [0.5, -4.0])
label.draw()


def f(x):
    return math.exp(x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-10,10])
graph.draw()

a = math.log(0.5)
dx = 2.1
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([math.log(0.5), f(math.log(0.5))], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = math.log(5)
dx = 0.4
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([math.log(5), f(math.log(5))], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

def f(x):
    return math.log(x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([0.001,10])
graph.draw()

a = 0.5
dx = 1.0
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(green)
tangent.draw()

point = Point([0.5, f(0.5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = 5
dx = 2.3
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(green)
tangent.draw()

point = Point([5, f(5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


def f(x):
    return x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(gray)
graph.setlinewidth(1)
graph.setdomain([-10,10])
graph.draw()


label = Label(r"$A$", [math.log(0.5), 0.5], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$B$", [math.log(5), 5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$A'$", [0.5, math.log(0.5)], alignment = "lt", offset = [2, 2] )
label.draw()

label = Label(r"$B'$", [5, math.log(5)], alignment = "lb", offset = [2, 3] )
label.draw()


restore()

endfigure()
