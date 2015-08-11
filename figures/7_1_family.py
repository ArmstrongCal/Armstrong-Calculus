from figures import *
import math

lbmargin = 15
rtmargin = 5
width = 150
height = 150

#Cvals = [-2.5, -2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
Cvals = [-3, -2, -1, 0, 1, 2, 3]

beginfigure("7_1_family", width, height)
setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
[0,0, 3.5, 6])

Grid([0,0.5,3.5], [0,0.5,6], color=lightgray).draw()
axes = Axes()
axes.draw()
axes.setticks([0,0.5,3], [0,0.5,6])
axes.drawticks()
axes.setlabels([0,1,3], [0,1,6])
axes.drawlabels()

dx = 0.25
dy = 0.2
for C in Cvals:
    f = Function(lambda x: 3+C*math.exp(-x/2.0))
    Graph(f, color=blue).draw()
    p = [1, f.value(1)]
    Box([p[0]-dx, p[1]-dy, 2*dx, 2*dy], fillcolor=white).fill()
    Label(r"$"+str(C)+"$", p, alignment="cc",color=darkmagenta).draw()


Label(r"$t$", [3.5,0], offset=[-3,3],alignment="rb").draw()
Label(r"$v$", [0,6], offset=[3,-3],alignment="lt").draw()

endfigure()


    
