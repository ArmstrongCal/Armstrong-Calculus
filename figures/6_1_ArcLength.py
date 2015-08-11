from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_1_ArcLength", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

grid = Grid([-1,6,5], 
            [-1,6,5], 
            color = gridcolor, linewidth = gridwidth)
#grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1, 1, 4])
axes.setvticks([2, 4, 5])
axes.drawticks()

label = Label("$x$", [4.5, 0.2])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [3.8, 4])
label.draw()

label = Label("$x_0$", [1, -0.5], alignment="cb")
label.draw()

label = Label("$x_1$", [2, -0.5], alignment="cb")
label.draw()

label = Label("$x_2$", [3, -0.5], alignment="cb")
label.draw()

label = Label("$x_3$", [4, -0.5], alignment="cb")
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(2)-f(1))/(2-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([1,2])
graph.draw()

def g(x):
    return f(2) + (f(3.0)-f(2))/(3.0-2)*(x-2)

graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3])
graph.draw()

def g(x):
    return f(3) + (f(4)-f(3))/(4-3)*(x-3)

graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([3,4])
graph.draw()


point = Point([1, f(1)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2, f(2)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3, f(3)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4, f(4)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

box = Box([1.7, f(2)-0.4, 1.6, f(3)-f(2)+0.8], color = gridcolor)
box.draw()

restore()
save()

## now for the adjacent figure

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [1.7,0.9,3.3,2.5])

outline = Box([1.7,0.9,1.6,1.6], color=gridcolor) # arguments are lower left corner, width and heigh
outline.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
##graph.setdomain([-1,5])
graph.draw()

def g(x):
    return f(1) + (f(2)-f(1))/(2-1)*(x-1)

cliptoboundingbox() 
graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([1,2])
graph.draw()

def g(x):
    return f(2) + (f(3.0)-f(2))/(3.0-2)*(x-2)

graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3])
graph.draw()

def g(x):
    return f(3) + (f(4)-f(3))/(4-3)*(x-3)

cliptoboundingbox() 
graph = Graph(Function(g))
graph.setcolor(green)
graph.setlinewidth(graphwidth)
graph.setdomain([3,4])
graph.draw()

line = Line([3,f(2)],[3,f(3)], linewidth = 1)
line.draw()

line = Line([2,f(2)],[3,f(2)], linewidth = 1)
line.draw()

point = Point([2, f(2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3, f(3)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$\triangle x$", [2.5, f(2)], alignment="ct", offset=[0,-2])
label.draw()

label = Label(r"$\triangle y$", [3, 0.5*(f(2)+f(3))], alignment="lc", offset=[2,0])
label.draw()

label = Label(r"$h$", [2.5, 0.5*(f(2)+f(3))], alignment="rb", offset=[-2,2])
label.draw()

label = Label(r"$L_{\mbox{\small{slice}}}$", [2.5, f(2.5)], alignment="lt", offset=[2,-2])
label.draw()


restore()


endfigure()
