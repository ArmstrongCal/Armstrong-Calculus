from figures import *

width = 120
height = 120
margin = 5

beginfigure("7.2.PA.tangents", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -2, 3.5, 3])

Grid([-0.5,0.5,3.5], [-2,0.5,3], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([-0.5,0.5,3.5], [-2,0.5,3])
axes.drawticks()
axes.setlabels([0,1,3], [-2,1,3])
axes.drawlabels()

def tangentline(a):
    yp = a-2
    y = 0.5*a*a-2*a+1
    f = Function(lambda x: y + yp*(x-a))
    dx = 0.25
    Graph(f, color=green, domain=[a-0.25, a+0.25]).draw()

for a in range(1,4):
    tangentline(a)

Label(r"$t$", [3.5,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,3], offset=[3,-3], alignment="lt").draw()

endfigure()
