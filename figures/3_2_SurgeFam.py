from figures import *
from defaults import *

width = standardwidth*2
height = standardheight
beginfigure("3_2_SurgeFam", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 7, 2])

line = Line([-1,0],[7,0], color=black, linewidth = 1.5)
line.draw()

line = Line([0,-2],[0,2], color=black, linewidth = 1.5)
line.draw()

#########

c = 3
d = 0.75

def f(x):
    return c*x*math.exp(-d*x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,7])
graph.draw()

a = 1/d
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\frac{1}{b}$", [a, -0.25], alignment = "ct", offset = [0,-2])
label.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"global max", [a, f(a)], alignment = "cb", offset = [0,4])
label.draw()

a = c/d * math.exp(-1)
line = Line([-0.1,a],[0.1,a], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\frac{a}{b}e^{-1}$", [-0.2,a], alignment = "rc", offset = [-2,0])
label.draw()

a = 2/d
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\frac{2}{b}$", [a, -0.25], alignment = "ct", offset = [0,-2])
label.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"inflection pt", [a, f(a)], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$g(x) = axe^{-bx}$", [5, 0.5], alignment = "lb", offset = [2,2])
label.draw()

restore()

endfigure()
