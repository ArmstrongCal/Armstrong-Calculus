from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_2_Act1Soln", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.5, -1, 1.5, 1])

grid = Grid([-1.5, 3, 1.5], [-1, 2, 1])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return x**3 + x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.5,2.5])
graph.draw()

label = Label(r"$p$", [0.8, 0.75])
label.draw()


point = Point([0, f(0)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-1.5, -1, 1.5, 1])

grid = Grid([-1.5, 3, 1.5], [-1, 2, 1])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 10, 2])
axes.drawticks()

line = Line([-1/math.sqrt(3), -0.05], [-1/math.sqrt(3), 0.05])
line.draw()

line = Line([1/math.sqrt(3), -0.05], [1/math.sqrt(3), 0.05])
line.draw()


def f(x):
    return x**3 - x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.5,2.5])
graph.draw()

label = Label(r"$p$", [1, 0.75])
label.draw()

label = Label(r"$-\sqrt{\frac{a}{3}}$", [-1/math.sqrt(3), -0.1], alignment="ct", offset = [-4,-1])
label.draw()

label = Label(r"$\sqrt{\frac{a}{3}}$", [1/math.sqrt(3), -0.1], alignment="ct", offset = [0,-1])
label.draw()

label = Label(r"$-\sqrt{a}$", [-1, -0.1], alignment="ct", offset = [0,-1])
#label.draw()

label = Label(r"$\sqrt{a}$", [1, -0.1], alignment="ct", offset = [0,-1])
#label.draw()


point = Point([0, f(0)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = -1/math.sqrt(3)

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-a, f(-a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
