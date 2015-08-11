from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Intro", 3*width, height)

margin = 10
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

circle = Circle([0,0], 4, color = graphcolor)
circle.draw()

p1 = Point([-3,math.sqrt(7)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([-3,-math.sqrt(7)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

box = Box([1, 1, 3, 3], color = gray)
box.draw()

label = Label(r"$A$", [-3,math.sqrt(7)], alignment = "lt", offset = [2, -2])
label.draw()

label = Label(r"$B$", [-3,-math.sqrt(7)], alignment = "lb", offset = [2, 4])
label.draw()

label = Label(r"$x^2 + y^2 = 16$", [-4.6,4], alignment = "lb", offset = [2, 2])
label.draw()

restore()

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [1, 1, 4, 4])


def f(x):
    return math.sqrt(16-x**2)

grid = Grid([1, 1, 4], [1, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,4])
graph.draw()

box = Box([1, 1, 3, 3], color = gray)
box.draw()

restore()

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
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

def f(x,y):
    return x*x*x - y*y*y - 6*x*y

Implicit(f, 0, color=graphcolor).draw()

label = Label(r"$x^3 - y^3 = 6xy$", [0.2,3], alignment = "lb", offset = [2, 2])
label.draw()


label = Label(r"$x$", [4.2,0.2], alignment = "lb", offset = [2, 2])
label.draw()

restore()


endfigure()
