from figures import *
from defaults import *

width = standardwidth*1.5
height = standardheight

beginfigure("4_2_RightMidSum", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 2, #  g = Function(lambda x: x*x*x), 
                domain = [1,3], fillcolor = boxcolor,
                style = RiemannSum.RIGHT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [4.5,5.5], fillcolor = boxcolor,
                style = RiemannSum.RIGHT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [7,8], fillcolor = boxcolor,
                style = RiemannSum.RIGHT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()


a = 1
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_0$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()


a = 2
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_1$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 3
label = Label(r"$x_2$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 4.5
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_i$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 5.5
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{i+1}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()



a = 7
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n-1}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 8
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

def f(x):
    return -0.05*(x-4)**3+7

point = Point([2, f(2)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3, f(3)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([5.5, f(5.5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([8, f(8)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$B_1$", [1.5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$B_2$", [2.5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$\cdots$", [3.75,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$B_{i+1}$", [5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$\cdots$", [6.25,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$y = f(x)$", [0.1,f(0.1)], alignment = "lb", offset = [3,3])
label.draw()

label = Label(r"$B_n$", [7.5,3], alignment = "cc", offset = [0,0])
label.draw()


restore()

#####################

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 2, #  g = Function(lambda x: x*x*x), 
                domain = [1,3], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [4.5,5.5], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [7,8], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()


a = 1
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_0$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()


a = 2
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_1$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 3
label = Label(r"$x_2$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 4.5
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_i$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 5.5
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{i+1}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()



a = 7
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n-1}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

a = 8
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1)
line.draw()

label = Label(r"$x_{n}$", [a, -0.25], alignment = "ct", offset = [0,-3])
label.draw()

def f(x):
    return -0.05*(x-4)**3+7

point = Point([2.5, f(2.5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([1.5, f(1.5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([5, f(5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([7.5, f(7.5)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$C_1$", [1.5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$C_2$", [2.5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$\cdots$", [3.75,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$C_{i+1}$", [5,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$\cdots$", [6.25,3], alignment = "cc", offset = [0,0])
label.draw()

label = Label(r"$y = f(x)$", [0.1,f(0.1)], alignment = "lb", offset = [3,3])
label.draw()

label = Label(r"$C_n$", [7.5,3], alignment = "cc", offset = [0,0])
label.draw()


restore()



endfigure()
