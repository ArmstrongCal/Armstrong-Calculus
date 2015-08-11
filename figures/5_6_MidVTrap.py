from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_6_MidVTrap", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -0.5, 2, 2])

axes = Axes()
axes.draw()

f = Function(lambda x: 0.5 + 0.375*(x-2)**2)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [0.5,1.5], fillcolor = boxcolor,
                style = RiemannSum.TRAP) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.3,1.7])
graph.draw()

label = Label(r"$T_1$", [1,0.5], alignment = "cc", offset = [0,0])
label.draw()

restore()

#####################

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                [-0.5, -0.5, 2, 2])

axes = Axes()
axes.draw()


f = Function(lambda x: 0.5 + 0.375*(x-2)**2)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [0.5,1.5], fillcolor = yellow,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.3,1.7])

graph.draw()

line = Line([0.5,0.5 + 0.375],[1.5,0.5 + 0.375], color=magenta, linewidth = 1.5)
line.draw()


label = Label(r"$M_1$", [1,0.5], alignment = "cc", offset = [0,0])
label.draw()


restore()


#####################

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                  [-0.5, -0.5, 2, 2])

axes = Axes()
axes.draw()


f = Function(lambda x: 0.5 + 0.375*(x-2)**2)

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.3,1.7])
graph.draw()

p = [0.5, 0]
q = [1.5, 0]
r = [1.5, 0.5]
s = [0.5, 1.25]

points = [p,q,r,s]
trapezoid = Polygon(points = points, fillcolor = yellow,
                   color = black, linewidth = 1, closed = True)
trapezoid.fill()
trapezoid.draw()

line = Line([1.5,0.5],[1.5, 0.875], color=black, linewidth = 1)
line.draw()

line = Line([0.5,1.25],[1.5,0.5], color=magenta, linewidth = 1.5)
line.draw()

line = Line([0.5,0.5 + 0.375],[1.5,0.5 + 0.375], color=magenta, linewidth = 1.5)
line.draw()

label = Label(r"$M_1$", [1,0.5], alignment = "cc", offset = [0,0])
label.draw()


restore()


endfigure()
