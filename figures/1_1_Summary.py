from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_1_Summary", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()


label = Label(r"$t$", [4.5, -0.5])
label.draw()

label = Label(r"$s$", [0.3, 4.5])
label.draw()

label = Label(r"$(a,s(a))$", [0.1, 1.2])
label.draw()

label = Label(r"$(b,s(b))$", [3.9, 2.25])
label.draw()

label = Label(r"$m = \frac{s(b)-s(a)}{b-a}$", [1.1, 2.9])
label.draw()


def f(x):
    return 0.1*x*(x+2)*(x-4) + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(4)-f(1))/(4-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,4.8])
graph.draw()


point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4, f(4)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
