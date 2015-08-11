from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_3_Act1Soln", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -6, 4, 10])

grid = Grid([-4,1,4], [-6, 2, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 8])
axes.drawticks()

axes.setlabels([-2, 5, 3], [2, 4, 4])
axes.drawlabels()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,3])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,-2])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([3,4])
graph.draw()

point = Point([-2, f(-2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-math.sqrt(2), f(-math.sqrt(2))], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([math.sqrt(2), f(math.sqrt(2))], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3,f(3)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$g$", [3,4], alignment = "lt", offset = [2, -2])
label.draw()

restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-4, -6, 4, 10])

grid = Grid([-4,1,4], [-6, 2, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 8])
axes.drawticks()

axes.setlabels([-2, 4, 2], [2, 4, 4])
axes.drawlabels()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,2])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,-2])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([2,4])
graph.draw()

point = Point([-2, f(-2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-math.sqrt(2), f(-math.sqrt(2))], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([math.sqrt(2), f(math.sqrt(2))], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2,f(2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$g$", [3,4], alignment = "lt", offset = [2, -2])
label.draw()

restore()

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-4, -6, 4, 10])

grid = Grid([-4,1,4], [-6, 2, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 8])
axes.drawticks()

axes.setlabels([-2, 3, 1], [2, 4, 4])
axes.drawlabels()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,1])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,-2])
graph.draw()

def f(x):
    return 0.3333 * x**3 - 2*x + 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([1,4])
graph.draw()

point = Point([-2, f(-2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-math.sqrt(2), f(-math.sqrt(2))], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([1,f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$g$", [3,4], alignment = "lt", offset = [2, -2])
label.draw()

restore()


endfigure()
