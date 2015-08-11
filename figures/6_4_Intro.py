from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_4_Intro", 3*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5, -0.5, 3.5, 3.5])

grid = Grid([-0.5,4,3.5], [-0.5,4,3.5], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:0.5*math.cos(2.5*x)+2)
a = 0.25
b = 2.5

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[a,b])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1.2,1.6], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

label = Label(r"$y = f(x)$", [0.1,2.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$a$", [a,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$b$", [b,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$f(x)$", [1.2,0.65], alignment = "rc", offset = [-3, 0] )
label.draw()

label = Label(r"$\triangle x$", [1.4,-0.3], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A = \int_a^b f(x) \, dx$", [1.35,1], alignment = "cc", offset = [0, 0] )
#label.draw()

restore()

##################

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-0.5,-0.5,3.5,3.5])

grid = Grid([-0.5,4,3.5], [-0.5,4,3.5], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

f = Function(lambda x: 1 + 0.3*x**2)

a = 0.25
b = 2.5

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[a,b])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = 1.5)
cliptoboundingbox()
graph.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1.2,1.6], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()


label = Label("$y$", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$t$", [3,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2.25,2.25], alignment = "rb", offset = [-4, 2] )
label.draw()

label = Label(r"$v(t)$", [1.2,0.65], alignment = "rc", offset = [-3, 0] )
label.draw()

label = Label(r"$\triangle t$", [1.4,-0.3], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$a$", [a,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$b$", [b,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

restore()


###################

save()

setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-1, -10, 11, 10])

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
graph.setdomain([4.5,4.59999])
graph.draw()

f = Function(lambda x: -1*math.sqrt(-10*(x-4.6)))
graph = Graph(f, color = red, linewidth = 1)
graph.setdomain([4.5,4.59999])
graph.draw()

label = Label(r"$\triangle x$", [4.25, -1.5], alignment = "ct", offset = [0,0])
label.draw()

label = Label(r"$\rho(x)$", [0.25, 1.1], alignment = "cb", offset = [0,1])
label.draw()

line = Line([10.1,0],[11,0], color=black, linewidth = 1.5)
line.draw()


restore()



endfigure()
