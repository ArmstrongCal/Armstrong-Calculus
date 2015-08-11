from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Act2", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 4, 3])

grid = Grid([-1, 0.5, 4], [-2, 0.5, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 2])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [-1, 1, 2])
axes.drawlabels()

#label = Label(r"$x^3 + y^2 - 2xy = 2$", [0.1,2.6], alignment = "lb", offset = [2, 2])
#label.draw()

def f(x,y):
    return y*y*y*y - 2*y*y*y - y*y + 2*y - x*x*x + 3*x*x - 2*x

Implicit(f, 0, color=graphcolor, initialdepth=6, depth=10).draw()

label = Label(r"$x$", [3.6,0.1], alignment = "lb", offset = [1, 1])
label.draw()

label = Label(r"$y$", [0.1,2.6], alignment = "lb", offset = [1, 1])
label.draw()

restore()

endfigure()
