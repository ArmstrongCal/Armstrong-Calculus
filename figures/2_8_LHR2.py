from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_8_LHR2", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -2.5, 4.5, 2.5])

grid = Grid([-0.5, 0.5, 4.5], [-2.5, 0.5, 2.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 1, 2])
axes.drawticks()

def f(x):
    return 0.5*(x**2-4)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.5,4.5])
graph.draw()

a = 2
dx = 1.4
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(darkgreen)
tangent.draw()

def f(x):
    return 0.25*(4-x**2)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.5,4.5])
graph.draw()

a = 2
dx = 1.4
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(green)
tangent.draw()

p1 = Point([2,0], 1.25)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

box = Box([1.5, -0.5, 1, 1], color = gray)
box.draw()

label = Label(r"$a$", [2,-0.1], alignment = "ct", offset = [0, -2])
label.draw()

label = Label(r"$g$", [3,-1.5], alignment = "rt", offset = [0, 0])
label.draw()

label = Label(r"$m = g'(a)$", [2.6,-0.7], alignment = "lb", offset = [2, 2])
label.draw()

label = Label(r"$f$", [2.5,2], alignment = "lb", offset = [2, 2])
label.draw()

label = Label(r"$m = f'(a)$", [2.5,0.5], alignment = "lb", offset = [2, 2])
label.draw()


restore()

#########################

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [1.5, -0.5, 2.5, 0.5])

axes = Axes()
axes.draw()

def f(x):
    return 0.5*(x**2-4)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,2.5])
graph.draw()

a = 2
dx = 0.5
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(darkgreen)
tangent.draw()

def f(x):
    return 0.25*(4-x**2)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,2.5])
graph.draw()

a = 2
dx = 0.5
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(green)
tangent.draw()

p1 = Point([2,0], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

box = Box([1.5, -0.5, 1, 1], color = gray)
box.draw()

label = Label(r"$a$", [2,-0.05], alignment = "ct", offset = [0, -1])
label.draw()

label = Label(r"$m = g'(a)$", [2.15,-0.15], alignment = "lb", offset = [0, 0])
label.draw()

label = Label(r"$m = f'(a)$", [2.15,0.2], alignment = "lb", offset = [2, 2])
label.draw()

restore()

endfigure()
