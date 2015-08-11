from figures import *
from defaults import *

width = 2*standardwidth
height = 60

beginfigure("4_2_Interval", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -3.5, 11, 1])

grid = Grid([-4, 8, 4], [-1.25, 8, 6])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
#grid.draw()

line = Line([-0.4,0],[10.4,0], color=black, linewidth = 1.5)
line.draw()

a = 0
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_0$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

label = Label(r"$a$", [a, 1], alignment = "cb", offset = [0,0])
label.draw()


a = 1
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_1$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 2
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_2$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a=3.5
label = Label(r"$\cdots$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 5
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_i$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 6
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{i+1}$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 5
line = Line([a,-3.1],[a,-2.3], color=blue, linewidth = 1)
line.draw()

a = 6
line = Line([a,-3.1],[a,-2.3], color=blue, linewidth = 1)
line.draw()

line = Line([5,-2.65], [6,-2.65], color=blue, linewidth = 1)
line.draw()

label = Label(r"$\triangle x$", [5.5, -3], alignment = "ct", offset = [0,-1.25])
label.draw()


a=7.5
label = Label(r"$\cdots$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 9
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n-1}$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

a = 10
line = Line([a,-0.4],[a,0.4], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n}$", [a, -1.25], alignment = "ct", offset = [0,0])
label.draw()

label = Label(r"$b$", [a, 1], alignment = "cb", offset = [0,0])
label.draw()

point = Point([-1.25, -1.25], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()


restore()

endfigure()
