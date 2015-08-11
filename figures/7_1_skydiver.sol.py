from figures import *
import math

dx = 50
lbmargin = 20
rtmargin = 5
width = 3.5 * dx + lbmargin + rtmargin
height = 6*dx + lbmargin + rtmargin

C = [-2.5, 2]

vtan = [[0.5, 1.0, 1.5, 2.0, 2.5], [5.0, 4.5, 4.0, 3.5]]

for i in range(2):
    beginfigure("7_1_activity.sol."+str(i), width, height)
    setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
                     [0,0, 3.5, 6])

    Grid([0,0.25,3.5], [0,0.25,6], color=lightgray).draw()
    axes = Axes()
    axes.draw()
    axes.setticks([0,0.5,3], [0,0.5,6])
    axes.drawticks()
    axes.setlabels([0,1,3], [0,1,6])
    axes.drawlabels()

    f = Function(lambda x: 3+C[i]*math.exp(-x/2.0))
    Graph(f, color=blue).draw()

    newpath()
    moveto(0,0)
    lineto(3.5,0)
    lineto(3.5,6)
    lineto(0,6)
    closepath()
    clip()
    newpath()

    dt = 0.25
    for v in vtan[i]:
        print v
        t = -2.0*math.log((v-3)/C[i])
        print t
        tangent = f.tangentline(t)
        Graph(tangent, domain=[t-dt, t+dt], color=red).draw()

    Label(r"$t$", [3.5,0], offset=[-3,3],alignment="rb").draw()
    Label(r"$v$", [0,6], offset=[3,-3],alignment="lt").draw()

    endfigure()
    
