from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_3_Intro", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -2, 4, 6])

grid = Grid([-4, 8, 4], [-2, 8, 6])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
#grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$x$", [5.2, 0.2])
label.draw()

label = Label(r"$f$", [3, 1])
label.draw()


def f(x):
    return -0.1*(x-2.5)*x*(x+2)*(x+2) + 2.75

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

label = Label(r"relative max", [-2, f(-2)], alignment = "cb", offset = [0,4])
label.draw()

a = -2
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$a$", [a, -0.75], alignment = "cb", offset = [0,0])
label.draw()

point = Point([-0.763086, f(-0.763086)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"relative min", [-0.763086, f(-0.763086)-0.25], alignment = "ct", offset = [4,-2])
label.draw()

a = -0.763086
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$b$", [a, -0.75], alignment = "cb", offset = [0,-1])
label.draw()

point = Point([1.63809, f(1.63809)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"global max", [1.63809, f(1.63809)], alignment = "cb", offset = [0,4])
label.draw()

a = 1.63809
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$c$", [a, -0.75], alignment = "cb", offset = [0,0])
label.draw()

restore()

endfigure()
