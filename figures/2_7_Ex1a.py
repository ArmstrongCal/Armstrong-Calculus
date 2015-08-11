from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Ex1a", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5, 1, 5], [-5, 1, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 1, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 1, 4])
axes.drawticks()

axes.setlabels([-4, 4, 4], # you can do this separately with seth(v)labels
               [-4, 4, 4])
axes.drawlabels()

#label = Label(r"$x^3 + y^2 - 2xy = 2$", [0.1,2.6], alignment = "lb", offset = [2, 2])
#label.draw()

def f(x,y):
    return x*x*x + y*y - 2*x*y - 2

Implicit(f, 0, color=graphcolor).draw()

line = Line([-0.806374-1, 0.97536], [-0.806374+1, 0.97536], color = tangentlinecolor, linewidth = graphwidth)
line.draw()

point = Point([-0.806374, 0.97536], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

line = Line([1.29664-1, 2.5219], [1.29664+1, 2.5219], color = tangentlinecolor, linewidth = graphwidth)
line.draw()

point = Point([1.29664, 2.5219], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


label = Label(r"$A$", [-0.806374, 0.97536], alignment = "rt", offset = [-4, -4])
label.draw()

label = Label(r"$B$", [1.29664, 2.5219], alignment = "lb", offset = [4, 4])
label.draw()



restore()

endfigure()
