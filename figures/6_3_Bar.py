from figures import *
from defaults import *

width = 2*standardwidth
height = 30

beginfigure("6_3_Bar", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1.5, 11, 1.5])

line = Line([-1,0],[0,0], color=black, linewidth = 1.5)
line.draw()

line = Line([0.1,1],[10.1,1], color=blue, linewidth = 1)
line.draw()

line = Line([0.1,-1],[10.1,-1], color=blue, linewidth = 1)
line.draw()

f = Function(lambda x: math.sqrt(10*x))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([0,0.1])
graph.draw()

f = Function(lambda x: -1*math.sqrt(10*x))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([0,0.1])
graph.draw()

f = Function(lambda x: math.sqrt(10*(x-10)))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([10,10.1])
graph.draw()

f = Function(lambda x: -1*math.sqrt(10*(x-10)))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([10,10.1])
graph.draw()

f = Function(lambda x: math.sqrt(-10*(x-10.2)))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([10.1,10.2])
graph.draw()

f = Function(lambda x: -1*math.sqrt(-10*(x-10.2)))
graph = Graph(f, color = blue, linewidth = 1)
graph.setdomain([10.1,10.2])
graph.draw()


f = Function(lambda x: math.sqrt(10*(x-4)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4,4.1])
graph.draw()

f = Function(lambda x: -1*math.sqrt(10*(x-4)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4,4.1])
graph.draw()

f = Function(lambda x: math.sqrt(10*(x-4.4)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4.4,4.5])
graph.draw()

f = Function(lambda x: -1*math.sqrt(10*(x-4.4)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4.4,4.5])
graph.draw()

f = Function(lambda x: math.sqrt(-10*(x-4.6)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4.5,4.5999])
graph.draw()

f = Function(lambda x: -1*math.sqrt(-10*(x-4.6)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4.5,4.5999])
graph.draw()

label = Label(r"$\triangle x$", [4.25, -1.5], alignment = "ct", offset = [0,0])
label.draw()

label = Label(r"$\rho(x)$", [0.25, 1.1], alignment = "cb", offset = [0,1])
label.draw()

line = Line([10.1,0],[11,0], color=black, linewidth = 1.5)
line.draw()


restore()

endfigure()
