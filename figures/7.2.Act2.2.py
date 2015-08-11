from figures import *

dx = 15
margin = 5
width = 8*dx + 2*margin
height = 8*dx + 2*margin

beginfigure("7.2.Act2.2", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 7, 6])

Grid([-1,1,7], [-2,1,6], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([-1,1,7], [-2,1,6])
axes.drawticks()
axes.setlabels([-1,1,7], [-2,1,6])
axes.drawlabels()


Label(r"$t$", [7,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,6], offset=[3,-3], alignment="lt").draw()


endfigure()
