from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_NotDiff", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 4, 4])

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3])
axes.drawhticks()
axes.setvticks([1, 3, 3])
axes.drawvticks()

axes.setlabels([1,3,3], # you can do this separately with seth(v)labels
               [1,3,3])
axes.drawlabels()

label = Label(r"$f$", [2, 2.5])
label.draw()

def f(x):
    return 2-x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.98,3])
graph.draw()

box = Box([0.8, 0.8, 0.4, 0.4], color = gray)
box.draw()

restore()
save()

## now for the adjacent figure

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [0.8,0.8,1.2,1.2])

outline = Box([0.8,0.8,0.4,0.4], color=gray) # arguments are lower left corner, width and heigh
outline.draw()

def f(x):
    return 2-x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.998,3])
graph.draw()

label = Label(r"$(1,1)$", [1.01,0.95])
label.draw()


restore()
endfigure()
