from figures import *
from defaults import *

width = standardwidth*1.5
height = standardheight

beginfigure("5_6_TRAP", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

axes.sethticks([1,2.333333,8]) 
axes.drawhticks()

#axes.sethlabels([1,7,8])
#axes.drawhlabels()

label = Label(r"$y = f(x)$", [0.1,10], alignment = "lb", offset = [3,3])
label.draw()

label = Label(r"$x_0$", [1,-1.5], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$x_1$", [3.3333333,-1.5], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$x_2$", [5.6666666,-1.5], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$x_3$", [8,-1.5], alignment = "cb", offset = [0,0])
label.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 3, #  g = Function(lambda x: x*x*x), 
                domain = [1,8], fillcolor = boxcolor,
                style = RiemannSum.TRAP) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()


def f(x):
    return -0.05*(x-4)**3+7

point = Point([1, f(1)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3.333333, f(3.333333)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([5.666666, f(5.666666)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([8, f(8)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$D_1$", [2.16666666,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$D_2$", [4.5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$D_3$", [6.83333333,3], alignment = "cc", offset = [0,0])
label.draw()



#label = Label(r"LEFT", [4.5,-1], alignment = "cc", offset = [0,0])
#label.draw()


restore()

endfigure()
