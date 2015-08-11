from figures import *
from prefs import *

width = standardwidth
height = standardheight
beginfigure("1_3_PA1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

axes.sethticks([1, 2.5, 3.5]) # you can do this in one line with setticks([], [])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)


label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

label = Label("$a$", [0.8, -0.7])
label.draw()

label = Label("$a+h$", [2.9, -0.7])
label.draw()


def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

point = Point([1.0, f(1.0)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3.5, f(3.5)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
