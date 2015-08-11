from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_6_MidTrapError", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0.2, 0, 1.8, 1.6])

p = [0.5, 0]
q = [1.5, 0]
r = [1.5, 0.59375]
s = [0.5, 1.34375]

points = [p,q,r,s]
trapezoid = Polygon(points = points, fillcolor = red,
                   color = black, linewidth = 1, closed = True)
trapezoid.fill()
trapezoid.draw()

f = Function(lambda x: 0.5+0.375*(x-2)**2)

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[0.5,1.5])
area.fill()
area.draw()

p = [0.5, 0]
q = [1.5, 0]
r = [1.5, 0.5]
s = [0.5, 1.25]

points = [p,q,r,s]
trapezoid = Polygon(points = points, fillcolor = yellow,
                   color = black, linewidth = 1, closed = True)
trapezoid.fill()
trapezoid.draw()


f = Function(lambda x: 0.5 + 0.375*(x-2)**2)

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.3,1.7])
graph.draw()

label = Label(r"$M_1$", [1,0.5], alignment = "cc", offset = [0,0])
label.draw()


restore()


endfigure()
