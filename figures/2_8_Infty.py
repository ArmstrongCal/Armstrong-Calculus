from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_8_Infty", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5, 1, 5], [-5, 1, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 1, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 1, 4])
axes.drawticks()


axes.setlabels([0, 1, 1], # you can do this separately with seth(v)labels
               [0, 1, 1])
axes.drawlabels()

label = Label(r"$f(x)=\frac{1}{x}$", [2,0.75], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 1/x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.01,5])
graph.draw()

def f(x):
    return 1/x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-5.1, -0.01])
graph.draw()

restore()

endfigure()
