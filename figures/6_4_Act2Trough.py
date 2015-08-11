from figures import *
from defaults import *

width = 1.5*standardwidth
height = standardheight
beginfigure("6_4_Act2Trough", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -6, 6, 3])

grid = Grid([-4, 10, 6], [-6, 9, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

line = Line([-3,0],[3,0], color=black, linewidth = 1)
line.draw()
line = Line([0,2],[0,-5], color=black, linewidth = 1)
line.draw()

p1 = [1.5,0]
q1 = [0,-4]
r1 = [-1.5,0]

points1 = [p1,q1,r1]
triangle1 = Polygon(points = points1, color = darkblue, fillcolor = gray, linewidth = 1, closed = True)
triangle1.setmiterlimit(1)
triangle1.draw()

line = Line([1,2],[4,2], color=darkblue, linewidth = 1)
line.draw()
line = Line([4,2],[2.5,-2], color=darkblue, linewidth = 1)
line.draw()
line = Line([2.5,-2], [0,-4], color=darkblue, linewidth = 1)
line.draw()
line = Line([-1.5,0], [1,2], color=darkblue, linewidth = 1)
line.draw()
line = Line([1.5,0], [4,2], color=darkblue, linewidth = 1)
line.draw()
line = Line([1,2], [1.6923,0.15385], color=darkblue, linewidth = 1)
line.draw()
line = Line([1.6923,0.15385], [2.5,-2], color=darkblue, linewidth = 1, dash=[2,2])
line.draw()


point = Point([0.75,-4], size = 1.5, fillcolor=pointcolor)
#point.fill()
#point.draw()

label = Label(r"$x^+$", [0.1,-4.5], alignment = "lc", offset = [2, 0] )
label.draw()

label = Label(r"$y^+$", [2.5,0], alignment = "lb", offset = [2, 2] )
label.draw()



restore()

endfigure()
