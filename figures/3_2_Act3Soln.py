from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("3_2_Act3Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -1, 7, 9])

grid = Grid([-5, 12, 7], [-1, 10, 9])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

#########

A = 8
c = 3.0
d = 0.7

line = Line([-5,A], [7,A], color=gray, linewidth = 1)
line.draw()

def f(x):
    return A/(1 + c*math.exp(-d*x))

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-5,7])
graph.draw()

label = Label(r"$y = L(x)$", [0.3,6.5], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$y = A$", [6.5, A], alignment = "rb", offset = [-2,2])
label.draw()

label = Label(r"$y = 0$", [6.5, 0], alignment = "rb", offset = [-2,2])
label.draw()

point = Point([0, f(0)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(0, \frac{A}{1+c})$", [0, f(0)], alignment = "rb", offset = [-4,2])
label.draw()

point = Point([-1/d * math.log(1/c), A/2], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(-\frac{1}{k} \ln(\frac{1}{c}), \frac{A}{2})$", [-1/d * math.log(1/c), A/2], alignment = "lt", offset = [2,-2])
label.draw()

restore()

endfigure()
