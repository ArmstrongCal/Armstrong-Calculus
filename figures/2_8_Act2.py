from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_8_Act2", 3*width, height)


save()
margin = 10
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


axes.setlabels([1, 1, 4], # you can do this separately with seth(v)labels
               [-2, 1, 2])
axes.drawlabels()

def f(x):
    return 0.125*(x**2-4)

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
    return -1*(4-x**2)

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

p1 = Point([2,0], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$f$", [4,1.5], alignment = "rb", offset = [-2, 2])
label.draw()

label = Label(r"$g$", [2.1,2], alignment = "lb", offset = [2, 2])
label.draw()

restore()

#########################

save()
margin = 10
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
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


axes.setlabels([1, 1, 4], # you can do this separately with seth(v)labels
               [-2, 1, 2])
axes.drawlabels()

def f(x):
    return 1.5-0.5*(x-2)**2

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

def f(x):
    return 2-0.5*(x-1)**2

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

p1 = Point([2,1.5], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$p$", [0.5,2], alignment = "rb", offset = [-2, 0])
label.draw()

label = Label(r"$q$", [0.5,0.5], alignment = "rb", offset = [-2, 0])
label.draw()

restore()

#########################

save()
margin = 10
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
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


axes.setlabels([1, 1, 4], # you can do this separately with seth(v)labels
               [-2, 1, 2])
axes.drawlabels()

def f(x):
    return 0.25*(x-2)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.5,4.5])
graph.draw()

def f(x):
    return -2*(x-2)**2

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
tangent.setcolor(darkgreen)
tangent.draw()

p1 = Point([2,0], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$s$", [3,-2], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$r$", [3,0.5], alignment = "lb", offset = [2, 2])
label.draw()

restore()

endfigure()
