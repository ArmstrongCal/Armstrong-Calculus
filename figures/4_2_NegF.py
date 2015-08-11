from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_2_NegF", 3*width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 3, 2])

grid = Grid([-1,4,3], [-1,3,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:math.cos(2.5*x)+0.5)
a = f.solve(1)
b = f.solve(1.7)
x0 = 2.8

rs = RiemannSum(f, 12, #  g = Function(lambda x: x*x*x), 
                domain = [0.2,x0], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()


graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,1.5], alignment = "lb", offset = [2, 2] )
label.draw()

line = Line([0.1,-0.6],[2.9,-0.6], linewidth = 1, color=black)
line.draw()

x1 = 0.2
line = Line([x1,-0.55],[x1,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$a$", [0.2,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([a,-0.55],[a,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$b$", [a,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([b,-0.55],[b,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$c$", [b,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([x0,-0.55],[x0,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$d$", [x0,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()



label = Label(r"$A_1$", [0.42,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_2$", [1.25,-0.2], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_3$", [2.35,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()


restore()

########

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-1, -1, 3, 2])

grid = Grid([-1,4,3], [-1,3,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:math.cos(2.5*x)+0.5)
a = f.solve(1)
b = f.solve(1.7)
x0 = 2.8

rs = RiemannSum(f, 24, #  g = Function(lambda x: x*x*x), 
                domain = [0.2,x0], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()


graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,1.5], alignment = "lb", offset = [2, 2] )
label.draw()

line = Line([0.1,-0.6],[2.9,-0.6], linewidth = 1, color=black)
line.draw()

x1 = 0.2
line = Line([x1,-0.55],[x1,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$a$", [0.2,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([a,-0.55],[a,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$b$", [a,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([b,-0.55],[b,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$c$", [b,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([x0,-0.55],[x0,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$d$", [x0,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()



label = Label(r"$A_1$", [0.42,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_2$", [1.25,-0.2], alignment = "cc", offset = [0, 0] )
#label.draw()

label = Label(r"$A_3$", [2.35,0.5], alignment = "cc", offset = [0, 0] )
#label.draw()


restore()

save()
margin = 10
setupcoordinates([2*width + margin,margin,3*width-margin,height-margin], 
                 [-1, -1, 3, 2])

grid = Grid([-1,4,3], [-1,3,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:math.cos(2.5*x)+0.5)
a = f.solve(1)
b = f.solve(1.7)
x0 = 2.8

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.2,a])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[a,b])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[b,x0])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,1.5], alignment = "lb", offset = [2, 2] )
label.draw()


label = Label(r"$A_1$", [0.42,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_2$", [1.25,-0.2], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_3$", [2.35,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

line = Line([0.1,-0.6],[2.9,-0.6], linewidth = 1, color=black)
line.draw()

x1 = 0.2
line = Line([x1,-0.55],[x1,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$a$", [0.2,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([a,-0.55],[a,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$b$", [a,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([b,-0.55],[b,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$c$", [b,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()

line = Line([x0,-0.55],[x0,-0.65], color=black, linewidth = 1)
line.draw()

label = Label(r"$d$", [x0,-0.95], alignment = "cb", offset = [0, 2] )
label.draw()


restore()


endfigure()
