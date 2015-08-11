from figures import *

width = 200
height = 200
margin = 5
beginfigure("example8", width, height)

save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5,1,5], [-5,1,5], color = lightgray)
grid.draw()

label = Label(r"{\bf Matt Boelkins}", [0,0], alignment = "cc")
label.draw()

import math
angle = 0
N = 10
dangle = 2*math.pi/N
for i in range(N):
    vector = Vector([2.5*math.cos(angle), 2.5*math.sin(angle)],
                    tail = [5*math.cos(angle), 5*math.sin(angle)], 
                    fillcolor=lightred, linewidth=0.5, arrowwidth = 2)
    vector.fill()
    angle += dangle

restore()
endfigure()
