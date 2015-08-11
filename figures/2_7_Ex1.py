from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Ex1", width, height)

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
    return x*x*x + y*y - 2*x*y - 2

Implicit(f, 0, color=graphcolor, initialdepth=6, depth = 10).draw()

line = Line([-2.5,1.325], [0.5,0.635], color = tangentlinecolor, linewidth = graphwidth)
line.draw()

point = Point([-1, 1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

#label = Label(r"$(-1,1)$", [-1,1], alignment = "cb", offset = [0, 2])
#label.draw()

label = Label(r"$x$", [3.2,0.2], alignment = "lb", offset = [2, 2])
label.draw()

label = Label(r"$y$", [0.2,3.2], alignment = "lb", offset = [2, 2])
label.draw()


restore()

endfigure()
