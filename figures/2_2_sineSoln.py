from figures import *
from defaults import*

width = 240
height = 80
beginfigure("2_2_sineSoln", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-2*pi, -2, 2*pi, 2])

xrange = [-2*pi, pi/2, 2*pi]
yrange = [-2, 1, 2]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks(xrange) 
axes.setvticks([-1,1,1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1,1,1])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()


label = Label(r"$-2\pi$", [-2*pi,-0.4], alignment = "ct", offset = [2, 2] )
label.draw()

label = Label(r"$-\pi$", [-pi,-0.4], alignment = "ct", offset = [-2, 2] )
label.draw()

label = Label(r"$\pi$", [pi,-0.5], alignment = "ct", offset = [2, 2] )
label.draw()

label = Label(r"$2\pi$", [2*pi,0.2], alignment = "cb", offset = [0, 2] )
label.draw()

### first original function graph

def f(x):
    return math.sin(x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

a = 3*pi/2
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = pi
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = pi/2
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = 0
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = -pi/2
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = -pi
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

a = -3*pi/2
dx = 0.7
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### grid for first derivative, second figure

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-2*pi, -2, 2*pi, 2])

xrange = [-2*pi, pi/2, 2*pi]
yrange = [-2, 1, 2]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$-2\pi$", [-2*pi,-0.4], alignment = "ct", offset = [2, 2] )
label.draw()

label = Label(r"$-\pi$", [-pi,-0.4], alignment = "ct", offset = [-2, 2] )
label.draw()

label = Label(r"$\pi$", [pi,-0.5], alignment = "ct", offset = [2, 2] )
label.draw()

label = Label(r"$2\pi$", [2*pi,-0.4], alignment = "ct", offset = [0, 2] )
label.draw()

axes.sethticks(xrange) 
axes.setvticks([-1,1,1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1,1,1])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()


def f(x):
    return math.cos(x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.draw()


restore()

endfigure()
