from figures import *
from defaults import *

width = standardwidth*1.6
height = standardheight*0.8

beginfigure("4_1_Ez3", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -2, 7.5, 2])

grid = Grid([-0.5, 0.5, 7.5], [-2, 0.5, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,7]) # you can do this in one line with setticks([], [])
axes.setvticks([-1,1,1])
axes.drawticks()

axes.setlabels([0,1,7], # you can do this separately with seth(v)labels
               [-1,1,1])
axes.drawlabels()

#label = Label("$x$", [3.2, 0.1])
#label.draw()

#label = Label("$y$", [0.1, 4.2])
#label.draw()

label = Label("$v$", [-1.2, 3.2])
label.draw()

def f(x):
    return x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1])
graph.draw()

def f(x):
    return math.sqrt(1-(x-1)**2)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,1.999])
graph.draw()

def f(x):
    return -1-(x-3)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3])
graph.draw()

def f(x):
    return -1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([3,4])
graph.draw()

def f(x):
    return x-5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([4,5])
graph.draw()

def f(x):
    return math.sqrt(1-(x-6)**2)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([5.001,6.999])
graph.draw()


label = Label(r"$y = v(t)$", [3,1], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
