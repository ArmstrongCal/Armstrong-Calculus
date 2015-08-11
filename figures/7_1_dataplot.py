from figures import *

lbmargin = 20
rtmargin = 5
dx = 75
width = 5.0*dx + rtmargin + lbmargin
height = 3.0*dx +  rtmargin + lbmargin

beginfigure("7_1_dataplot", width, height)
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
Label(r"$\displaystyle\frac{dv}{dt}$", [0,1.5], offset=[3,-3], alignment="lt").draw()

endfigure()
