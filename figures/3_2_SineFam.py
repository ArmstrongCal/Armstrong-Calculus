from figures import *
from defaults import *

width = standardwidth*1.6
height = standardheight*1.2
beginfigure("3_2_SineFam", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -2, 4, 8])

line = Line([-4,0],[4,0], color=black, linewidth = 1.5)
line.draw()

line = Line([0,-2],[0,8], color=black, linewidth = 1.5)
line.draw()

#########

def f(x):
    return 2*math.sin(3*(x-pi/6))+5

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([pi/6,5*pi/6])
graph.draw()

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4, pi/6])
graph.draw()

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([5*pi/6,4])
graph.draw()

a = pi/6
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$c$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


a = 5*pi/6
line = Line([a,-0.1],[a,0.1], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$c + \frac{2\pi}{b}$", [a, -0.25], alignment = "ct", offset = [0,-2])
label.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


a = 5
line = Line([-0.1,a],[0.1,a], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$d$", [-0.1, a], alignment = "rc", offset = [-2,0])
label.draw()

a = 7
line = Line([-0.1,a],[0.1,a], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$d+a$", [-0.1, a+0.25], alignment = "rc", offset = [-2,0])
label.draw()


label = Label(r"$f(t) = a\sin(b(t-c)) + d$", [-4, 2], alignment = "lb", offset = [2,2])
label.draw()

restore()

endfigure()
