from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_8_Act1Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 2, 2])

grid = Grid([-5, 1, 2], [-5, 1, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return -2 + 3*(x+1) + (x+1)**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-5,0])
graph.draw()


def f(x):
    return -2 + 3*(x+1)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-5,2])
graph.draw()

point = Point([-1, -2], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$y = g(x)$", [-2.7,1], alignment = "rb", offset = [-2, 2]  )
label.draw()

label = Label(r"$y = L(x)$", [-1.85,-5], alignment = "lb", offset = [2, 2]  )
label.draw()

label = Label(r"$(-1,-2)$", [-1,-2], alignment = "rb", offset = [-4, 4]  )
label.draw()


restore()

endfigure()
