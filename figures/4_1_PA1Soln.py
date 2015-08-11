from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_PA1Soln", 2*width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.25, -1, 2.5, 9])

grid = Grid([-0.25, 0.25, 2.5], [-1, 1, 9])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,2,8])
axes.drawticks()

axes.setlabels([0,1,2], # you can do this separately with seth(v)labels
               [0,4,8])
axes.drawlabels()

label = Label("mph", [0.1,8], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2.1,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

f = Function(lambda x:3)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [0.25,1.5], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

def f(x):
    return 3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2.5])
graph.draw()

label = Label(r"$v(t) = 3$", [1.5, 3], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$A = 3 \cdot 1.25 = 3.75$", [0.5*1.25+0.25, 1.5], alignment = "cc", offset = [0,0], scale = 0.75)
label.draw()

restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.25, -1, 2.5, 9])

grid = Grid([-0.25, 0.25, 2.5], [-1, 1, 9])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,2,8])
axes.drawticks()

axes.setlabels([0,1,2], # you can do this separately with seth(v)labels
               [0,4,8])
axes.drawlabels()

label = Label("miles", [0.1,8], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2.1,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 3*x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2.5])
graph.draw()

a = 0.25
line = Line([a,0],[a,f(a)], color=boxcolor, linewidth = 1.5)
line.draw()

point = Point([0.25, f(0.25)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$s(0.25)=0.75$", [0.25, 0.5*f(0.25)], alignment = "lc", offset = [2,0], scale = 0.75)
label.draw()

a = 1.5
line = Line([a,0],[a,f(a)], color=boxcolor, linewidth = 1.5)
line.draw()

point = Point([1.5, f(1.5)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$s(1.5)=4.5$", [1.5, 0.5*f(1.5)], alignment = "lc", offset = [2,0], scale = 0.75)
label.draw()

label = Label(r"$s(t) = 3t$", [2, f(2)], alignment = "rb", offset = [-2,2])
label.draw()

restore()

endfigure()
