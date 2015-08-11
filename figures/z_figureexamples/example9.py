from figures import *

width = 200
height = 200
margin = 5
beginfigure("example9", width, height)

save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5,1,5], [-5,1,5], color = lightgray)
grid.draw()

Axes().draw()

import math
save()
cliptoboundingbox()
C = -2
while C <= 2:
    graph = Graph(Function(lambda x: x-1 + C*math.exp(-x)), 
                  color = lightred)
    graph.draw()
    C += 0.2
restore()

def f(x,y):
    return x-y
field = SlopeField(f, [-5,1,5], [-5,1,5], color = blue)
field.draw()

restore()
endfigure()
