from figures import *
from defaults import *

width = 180
height = 180

beginfigure("2_6_GenInv", width, height)

margin = 20
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 10, 10])

grid = Grid([-4, 1, 10], [-4, 1, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$m = g'(b)$", [7,3], alignment = "lb", offset = [2, 2] )
label.draw()


label = Label(r"$y = f(x)$", [-3.9,4.25])
label.draw()

label = Label(r"$y = g(x)$", [2, -3])
label.draw()


def f(x):
    return x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(gray)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,10])
graph.draw()

def f(x):
    return 0.25*x**3 + 4

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,10])
graph.draw()

a = 2
dx = 1
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([2, f(2)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


def f(x):
    return (4*x-16)**(0.33)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([4,10])
graph.draw()

a = 6
dx = 3
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(thisgraphwidth)
tangent.setcolor(green)
tangent.draw()

point = Point([6, f(6)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


def f(x):
    return -1*(16-4*x)**(0.33)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,3.9999])
graph.draw()

label = Label(r"$(a,b)$", [2,6], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$m = f'(a)$", [3,9], alignment = "lt", offset = [2, -2] )
label.draw()


label = Label(r"$(b,a)$", [6,2], alignment = "rb", offset = [-2, 2] )
label.draw()


restore()

endfigure()
