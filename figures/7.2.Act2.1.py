from figures import *

dx = 23
margin = 5
width = 8*dx + 2*margin
height = 5*dx + 2*margin

beginfigure("7.2.Act2.1", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2.5, 6, 2.5])

gsave()
cliptoboundingbox()
Grid([-2,1,7], [-2,1,3], color=lightgray).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-2,1,6], [-2,1,2])
axes.drawticks()
axes.setlabels([-2,1,6], [-2,1,2])
axes.drawlabels()


Label(r"$y$", [6,0], offset=[-3,3], alignment="rb").draw()
Label(r"$\frac{dy}{dt}$", [0,2.5], offset=[3,-3], alignment="lt").draw()


endfigure()
