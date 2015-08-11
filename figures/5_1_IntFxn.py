from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_1_IntFxn", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5*pi, -2, 2.5*pi, 2])

xrange = [-0.5*pi, pi/2, 2.5*pi]
yrange = [-2, 0.5, 2]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,pi/2,2*pi]) 
axes.setvticks([-1,1,1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1,1,1])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()


label = Label(r"$y=f(t)$", [2*pi,1.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$\pi$", [pi,0.1], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$2\pi$", [2*pi,0.1], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$x$", [1.25,-0.1], alignment = "ct", offset = [0, -2] )
label.draw()

### first original function graph

def f(x):
    return math.cos(x)+0.5

area = AreaBetweenCurves(Function(f), fillcolor = lightblue, domain=[0,1.25])
area.fill()
area.draw()


cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.draw()

point = Point([1.25, f(1.25)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

###

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-0.5*pi, -0.5, 2.5*pi, 3.5])

xrange = [-0.5*pi, pi/2, 2.5*pi]
yrange = [-0.5, 0.5, 3.5]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,pi/2,2*pi]) 
axes.setvticks([1,1,3])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([1,2,3])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()


label = Label(r"$\pi$", [pi,0.1], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$2\pi$", [2*pi,0.1], alignment = "cb", offset = [0, 2] )
label.draw()


def f(x):
    return math.sin(x)+0.5*x

cliptoboundingbox()
graph = Graph(Function(f), color = graphcolor, linewidth = graphwidth)
graph.setdomain([-0.5*pi,2*pi])
graph.draw()

line = Line([1.25,0],[1.25,f(1.25)], color = darkgray)
line.draw()

point = Point([1.25, f(1.25)], 2)
point.setfillcolor(cyan)
point.fill()
point.draw()

label = Label(r"$x$", [1.25,-0.1], alignment = "ct", offset = [0, -2] )
label.draw()

label = Label(r"$A(x)$", [1,0.5*f(1.25)], alignment = "lc", offset = [4, 0] )
label.draw()

restore()

endfigure()
