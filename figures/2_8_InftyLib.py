from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_8_InftyLib", 3*width, height)


save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 10, 10])

grid = Grid([-5, 15, 10], [-5, 15, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 2, 8]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 8])
axes.drawticks()

axes.setlabels([-4, 4, 8], # you can do this separately with seth(v)labels
               [-4, 4, 8])
axes.drawlabels()

label = Label(r"$y = e^x$", [2.5, 8.5])
label.draw()

label = Label(r"$y = \ln(x)$", [0.5, -4.0])
label.draw()


def f(x):
    return math.exp(x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-5,10])
graph.draw()

def f(x):
    return math.log(x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([0.001,10])
graph.draw()

restore()

#########################

save()
margin = 10
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-6, -96, 6, 96])

grid = Grid([-6, 12, 6], [-96, 192, 96])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 2, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-64, 32, 64])
axes.drawticks()

axes.setlabels([-2, 2, 2], # you can do this separately with seth(v)labels
               [-64, 64, 64])
axes.drawlabels()

label = Label(r"$y = f(x)$", [-3.75, 32])
label.draw()

label = Label(r"$y = g(x)$", [-3.75, -90])
label.draw()


def f(x):
    return x*x*x - 16*x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-8,8])
graph.draw()

def f(x):
    return x*x*x*x - 16*x*x - 8

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-8,8])
graph.draw()


restore()

#########################

save()
margin = 10
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-20,-2,20,2])

grid = Grid([-20, 40, 20], [-2, 4, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-15, 5, 15]) # you can do this in one line with setticks([], [])
axes.setvticks([-1.5, 0.5, 1.5])
axes.drawticks()


axes.setlabels([10, 10, 15], # you can do this separately with seth(v)labels
               [1, 2, 2])
axes.drawlabels()

def f(x):
    return math.sin(x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setN(1000)
graph.setdomain([-20,20])
graph.draw()

label = Label(r"$y = \sin(x)$", [5, 1.1])
label.draw()

restore()

endfigure()
