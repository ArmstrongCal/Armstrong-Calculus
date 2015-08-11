from figures import *

width = 120
height = 120
margin = 8
lbmargin = 15

x0 = 0
x1 = 1.2
y0 = 0
y1 = 8

N = 2
beginfigure("7.3.euler.empty.2", width, height)
setupcoordinates([lbmargin+5, lbmargin, width-margin, height-margin],
                 [x0, y0, x1, y1])

xrange = [x0,0.2,x1]
yrange = [y0,1,y1]
Grid(xrange, yrange, color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks(xrange,yrange)
axes.setlabels([x0, 0.4, x1+0.1],[y0,2, 8])
axes.drawticks()
axes.drawlabels()

Label(r"$t$", [x1,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,y1], offset=[3,-3], alignment="lt").draw()

endfigure()
