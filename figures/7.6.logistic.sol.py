from figures import *
width=200
height=150

x0 = 0
x1 = 200
y0 = 0
y1 = 15
beginfigure("7_6_logistic_sol", width, height)
setupcoordinates([15, 15, width-10, height-5],
                 [x0, y0, x1, y1])

Grid([x0,20,x1], [y0, 3, y1], color=lightgray).draw()

axes=Axes()
axes.draw()
axes.setticks([x0,20,x1], [y0,3,y1])
axes.drawticks()
axes.setlabels([x0,40,x1], [y0, 3, y1])
axes.drawlabels()

from math import *
k = 0.002
N = 12.5
P0 = 6.084
gsave()
cliptoboundingbox()
Graph(Function(lambda t: P0*N/((N-P0)*exp(-k*N*t) + P0)), color=blue).draw()
grestore()

Label(r"$t$", [x1,0], offset=[-3,3],alignment="rb").draw()
Label(r"$P$", [0,y1], offset=[3,-3],alignment="lt").draw()

endfigure()




