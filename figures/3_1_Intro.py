from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Intro", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -10, 2.5, 50])

grid = Grid([-0.5, 0.5, 2.5], [-10, 10, 50])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 10, 40])
axes.drawticks()

axes.setlabels([0, 1, 2], # you can do this separately with seth(v)labels
               [0, 10, 40])
axes.drawlabels()

def f(x):
    return -16*x**2 + 24*x + 32

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2.5])
graph.draw()


label = Label(r"$y=s(t)$", [1.25, 40])
label.draw()


point = Point([0.75, f(0.75)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$V$", [0.75, f(0.75)], alignment = "rb", offset = [0,3])
label.draw()

restore()

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 8, 4], [-4, 8, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$x$", [5.2, 0.2])
label.draw()

label = Label(r"$y=g(x)$", [-3, -3])
label.draw()


def f(x):
    return -0.1*(x-2.5)*x*(x+2)*(x+2) + 0.75

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,4])
graph.draw()

point = Point([-2, f(-2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(a,g(a))$", [-2, f(-2)], alignment = "rb", offset = [6,4])
label.draw()

point = Point([-0.763086, f(-0.763086)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(b,g(b))$", [-0.763086, f(-0.763086)-0.25], alignment = "rt", offset = [3,-4])
label.draw()

point = Point([1.63809, f(1.63809)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(c,g(c))$", [1.63809, f(1.63809)], alignment = "lb", offset = [2,4])
label.draw()

restore()

endfigure()
