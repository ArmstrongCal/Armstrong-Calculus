from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Act1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 1, 4], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([-3, 3, 3], # you can do this separately with seth(v)labels
               [-3, 3, 3])
axes.drawlabels()

#label = Label(r"$x^3 + y^2 - 2xy = 2$", [0.1,2.6], alignment = "lb", offset = [2, 2])
#label.draw()

def f(x,y):
    return (y*y*y*y*y - 5*y*y*y + 4*y) - x

Implicit(f, 0, color=graphcolor, initialdepth=6, depth=10).draw()

label = Label(r"$x$", [3.6,0.2], alignment = "lb", offset = [1, 1])
label.draw()

label = Label(r"$y$", [0.2,3.6], alignment = "lb", offset = [1, 1])
label.draw()

restore()

endfigure()
