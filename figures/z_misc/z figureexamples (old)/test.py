from figures import *
from colors import *

width = 300
height = 200
beginfigure("1_2_PA1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, 0, 3, 4])

grid = Grid([-2, 0.5, 3], [0, 0.5, 4])
grid.setcolor(gridcolor)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return -(x*x-4)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(2)
graph.setdomain([-2,1])
graph.draw()

graph.setfunction( Function(lambda x : -x+1))
graph.setdomain([1,3])
graph.draw()

p1 = Point([0,4], 3)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1.setpoint([1,2])
p1.fill()
p1.draw()

p2 = Point([0,1], 3)
p2.setfillcolor(graphcolor)
p2.fill()
p2.draw()

p2.setpoint([1,3])
p2.fill()
p2.draw()

restore()

endfigure()
