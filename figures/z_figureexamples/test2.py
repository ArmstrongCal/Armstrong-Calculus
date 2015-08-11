from figures import *

width = 300
height = 200
beginfigure("test2", width, height)
save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, 0, 3, 4])

grid = Grid([-2, 0.5, 3], [0, 0.5, 4], color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

graph = Graph(Function(lambda x:-(x*x-4)), color=orange, domain=[-2,1])
graph.draw()

graph = Graph(Function(lambda x:x+1), color = orange, domain=[1,3])
graph.draw()

point = Point([0,1], size=3, fillcolor=orange)
point.fill()
point.draw()

point.setpoint([1,3])
point.fill()
point.draw()

point = Point([0,4], size=3, fillcolor=white)
point.fill()
point.draw()

point.setpoint([1,2])
point.fill()
point.draw()

restore()
endfigure()
