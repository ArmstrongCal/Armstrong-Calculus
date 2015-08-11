from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Act1Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-8, -36, 4, 36])

grid = Grid([-8, 12, 4], [-36, 72, 36])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

line = Line([2,-36], [2,36], color=gray)
line.draw()

axes.sethticks([-6, 2, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 50, 36])
axes.drawticks()


axes.setlabels([-6, 2, 2], # you can do this separately with seth(v)labels
               [0, 50, 36])
axes.drawlabels()

label = Label(r"$g$", [3,20], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 0.33*x**3+2*x**2+x+6*math.log(2-x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-8,1.999])
graph.draw()

def f(x):
    return 0.33*x**3+2*x**2+x+6*math.log(x-2)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2.001,4])
graph.draw()
restore()

endfigure()
