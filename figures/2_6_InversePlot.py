from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_6_InversePlot", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 0.5, 4], [-4, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([-2, 2, 2], # you can do this separately with seth(v)labels
               [-2, 2, 2])
axes.drawlabels()

label = Label(r"$y = f(x)$", [1.0, 3.5])
label.draw()

label = Label(r"$y = f^{-1}(x)$", [0.4, -3])
label.draw()


def f(x):
    return 2**x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,4])
graph.draw()

def f(x):
    return math.log(x)/(math.log(2))

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([0.05,4])
graph.draw()

def f(x):
    return x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkgray)
graph.setlinewidth(1)
graph.setdomain([-4,4])
graph.draw()

p1 = Point([-1,0.5], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([0.5,-1], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$(-1,\frac{1}{2})$", [-1,0.5], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$(\frac{1}{2},-1)$", [0.5,-1], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$y=x$", [-3,-3.5], alignment = "lc", offset = [2, 0] )
label.draw()

restore()

endfigure()
