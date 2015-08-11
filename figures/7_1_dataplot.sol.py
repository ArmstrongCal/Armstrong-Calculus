from figures import *

lbmargin = 20
rtmargin = 5
dx = 75
width = 5.0*dx + rtmargin + lbmargin
height = 3.0*dx +  rtmargin + lbmargin

beginfigure("7_1_dataplot.sol.1", width, height)
setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
                 [0, -1.5, 5, 1.5])

Grid([0,0.5,5], [-1.5,0.5,1.5], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([0,0.5,5], [-1.5,0.5,1.5])
axes.drawticks()
axes.setlabels([0,1,5], [-1.5,0.5,1.5])
axes.drawlabels()

Label(r"$v$", [5,0], offset=[-3,3], alignment="rb").draw()
Label(r"$v'$", [0,1.5], offset=[3,-3], alignment="lt").draw()

def f(x):
    return 1.5 - 0.5*x

func = Function(f) 
Graph(func, color=darkmagenta).draw()

v = [0.5, 1.0, 1.5, 2.0, 2.5, 3.5, 4.0, 4.5, 5.0]
for p in v:
    point = Point([p, f(p)], fillcolor=red)
    point.fill()
    point.draw()

endfigure()


