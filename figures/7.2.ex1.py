from figures import *

margin = 5
width = 120
height = 120

beginfigure("7.2.ex.1", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

Grid([-4, 1, 4], [-4,1,4], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([-4,1,4], [-4, 1, 4])
axes.drawticks()
axes.setlabels([-4,1,4], [-4, 1, 4])
axes.drawlabels()

Label(r"$t$", [4,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,4], offset=[3,-3], alignment="lt").draw()


endfigure()
