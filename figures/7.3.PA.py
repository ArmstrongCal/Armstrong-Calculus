from figures import *

width = 120
height = 120
margin = 5
lbmargin = 15

x0 = 0
x1 = 7
y0 = 0
y1 = 7

beginfigure("7.3.PA", width, height)
setupcoordinates([lbmargin, lbmargin, width-margin, height-margin],
                 [x0, y0, x1, y1])

xrange=[x0,1,x1]
yrange=[y0,1,y1]
Grid(xrange, yrange, color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks(xrange, yrange)
axes.drawticks()
axes.setlabels(xrange, yrange)
axes.drawlabels()

Label(r"$t$", [x1,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,y1], offset=[3,-3], alignment="lt").draw()

endfigure()
