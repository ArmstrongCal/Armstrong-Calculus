from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_7_Circle", width, height)

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

label = Label(r"$m_t = -\frac{a}{b}$", [1,4.2], alignment = "lb", offset = [2, 2])
label.draw()

circle = Circle([0,0], 4, color = graphcolor)
circle.draw()

def f(x):
    return math.sqrt(16-x**2)

cliptoboundingbox() 
a = 2.4
dx = 1.8
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

line = Line([0,0], [a,f(a)], color = gray, linewidth = 1.25)
line.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(a,b)$", [a,f(a)], alignment = "lb", offset = [2, 0])
label.draw()

label = Label(r"$m_r = \frac{b}{a}$", [1,0.5], alignment = "lb", offset = [2, 2])
label.draw()




restore()

endfigure()
