from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("3_2_Act2Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 3, 2])

grid = Grid([-1, 4, 3], [-2, 4, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()



#########

c = 1.5
d = 1.7

line = Line([-1,c], [3,c], color=gray, linewidth = 1)
line.draw()

def f(x):
    return c - c*math.exp(-d*x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

label = Label(r"$h(x) = a(1-e^{-bx})$", [0.35, 0.4], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$a$", [0, c], alignment = "rb", offset = [-2,2])
label.draw()

restore()

endfigure()
