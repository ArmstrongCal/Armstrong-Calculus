from figures import *
from defaults import *

width = standardwidth*1.6
height = standardheight*1.2
beginfigure("3_1_Ex2", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2.5, -2, 2.5, 6])

line = Line([-2.5,0],[2.5,0], color=black, linewidth = 1.5)
line.draw()

line = Line([0,-2],[0,10], color=black, linewidth = 1.5)
line.draw()

#########

a = -math.sqrt(3)
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$-\sqrt{3}$", [a-0.2, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = -math.sqrt(1.5)
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$-\sqrt{1.5}$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

a = math.sqrt(3)
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\sqrt{3}$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = math.sqrt(1.5)
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\sqrt{1.5}$", [a-0.1, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

def f(x):
    return 0.25*(0.6*x**5 - 3*x**3) + 3.5

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.5,2.5])
graph.draw()

a = -math.sqrt(3)

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$A$", [a, f(a)], alignment = "lb", offset = [4,4])
label.draw()

a = math.sqrt(3)

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$E$", [a, f(a)], alignment = "lt", offset = [4,-4])
label.draw()


a = math.sqrt(1.5)

point = Point([a, f(a)], 2)
point.setfillcolor(orange)
point.fill()
point.draw()

label = Label(r"$D$", [a, f(a)], alignment = "lb", offset = [4,4])
label.draw()


a = -math.sqrt(1.5)

point = Point([a, f(a)], 2)
point.setfillcolor(orange)
point.fill()
point.draw()

label = Label(r"$B$", [a, f(a)], alignment = "lb", offset = [4,4])
label.draw()


a = 0

point = Point([a, f(a)], 2)
point.setfillcolor(green)
point.fill()
point.draw()

label = Label(r"$C$", [a, f(a)], alignment = "lb", offset = [4,4])
label.draw()


label = Label(r"$f$", [2.3, f(2.3)], alignment = "rb", offset = [-4,4])
label.draw()

restore()

endfigure()
