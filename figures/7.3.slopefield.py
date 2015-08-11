from figures import *

width=120
height=120
lbmargin = 20
rtmargin = 5

beginfigure("7.3.slopefield", width, height)
setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
                 [0,0,8, 8])

Grid([0, 1, 8], [0, 1, 8], color=lightgray).draw()
axes = Axes()
axes.draw()
axes.setticks([0,1,8], [0,1,8])
axes.setlabels([0,2,8], [0,2,8])
axes.drawticks()
axes.drawlabels()

Label(r"$y$", [0,8], offset=[3,-3], alignment="lt").draw()
Label(r"$t$", [8,0], offset=[-3,3], alignment="rb").draw()


endfigure()
