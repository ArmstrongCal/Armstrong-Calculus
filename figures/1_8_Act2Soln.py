from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_8_Act2Soln", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -4, 6, 4])

grid = Grid([-2, 1, 6], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.setlabels([2, 2, 3], # you can do this separately with seth(v)labels
               [2, 2, 3])
axes.drawlabels()

label = Label("$x$", [5.2, 0.2])
label.draw()

label = Label("$y$", [0.1, 3.2])
label.draw()

label = Label(r"$y=f(x)$", [3.8, 1.75])
label.draw()

def f(x):
    return -0.16667*x**3 + x**2 - 1 + 0.16667*8 - 4

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,6])
graph.draw()

a = 2
dx = 1.5
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([2, f(2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()



restore()

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-2, -4, 6, 4])

grid = Grid([-2, 1, 6], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.setlabels([2, 2, 3], # you can do this separately with seth(v)labels
               [2, 2, 3])
axes.drawlabels()

label = Label(r"$x$", [5.2, 0.2])
label.draw()

label = Label(r"$y$", [0.1, 3.2])
label.draw()

label = Label(r"$y=f'(x)$", [2.5, 2.2])
label.draw()


def f(x):
    return -0.5*x*(x-4)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,6])
graph.draw()

restore()

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-2, -4, 6, 4])

grid = Grid([-2, 1, 6], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.setlabels([2, 2, 3], # you can do this separately with seth(v)labels
               [2, 2, 3])
axes.drawlabels()

label = Label("$x$", [5.2, 0.2])
label.draw()

label = Label("$y$", [0.1, 3.2])
label.draw()


def f(x):
    return -0.5*x*(x-4)

cliptoboundingbox()
derivative = Function(f).differentiate()
graph = Graph(derivative, color=lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,6])
graph.draw()

label = Label(r"$y=f''(x)$", [1.5, 1.2])
label.draw()

restore()


endfigure()
