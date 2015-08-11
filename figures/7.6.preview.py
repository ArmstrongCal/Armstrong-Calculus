from figures import *
width=150
height=150

x0 = 0
x1 = 4
y0 = 0
y1 = 4
beginfigure("7_6_preview", width, height)
setupcoordinates([15, 15, width-7, height-5],
                 [x0, y0, x1, y1])

Grid([x0,1,x1], [y0, 1, y1], color=lightgray).draw()

axes=Axes()
axes.draw()
axes.setticks([x0,1,x1], [y0,1,y1])
axes.drawticks()
axes.setlabels([x0,2,x1+0.001], [y0, 1, y1])
axes.drawlabels()

Label(r"t", [x1,0], offset=[-3,3],alignment="rb").draw()
Label(r"P", [0,y1], offset=[3,-3],alignment="lt").draw()


endfigure()
