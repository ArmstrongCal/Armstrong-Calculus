from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("2_6_arcsine", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.75*pi, -0.75*pi, 0.75*pi, 0.75*pi])


grid = Grid([-0.75*pi, 0.25*pi, 0.75*pi], [-0.75*pi, 0.25*pi, 0.75*pi], color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-0.5*pi, 0.25*pi, 0.5*pi]) 
axes.setvticks([-0.5*pi, 0.25*pi, 0.5*pi])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

label = Label(r"$-\frac{\pi}{2}$", [-0.5*pi-0.1,-0.3], alignment = "ct", offset = [0, 2] )
label.draw()

label = Label(r"$\frac{\pi}{2}$", [0.5*pi,-0.3], alignment = "ct", offset = [0, 2] )
label.draw()

label = Label(r"$-\frac{\pi}{2}$", [-0.3, -0.5*pi], alignment = "rc", offset = [2, 0] )
label.draw()

label = Label(r"$\frac{\pi}{2}$", [-0.3, 0.5*pi], alignment = "rc", offset = [2, 0] )
label.draw()


def f(x):
    return x
 
graph = Graph(Function(f))
graph.setdomain([-0.75*pi, 0.75*pi])
graph.setcolor(gray)
graph.draw()

def f(x):
    return math.sin(x)
 
graph = Graph(Function(f))
graph.setdomain([-0.5*pi, 0.5*pi])
graph.setcolor(graphcolor)
graph.draw()

point = Point([-0.5*pi, -1], 1.5)
point.setfillcolor(graphcolor)
point.fill()
point.draw()

point = Point([0.5*pi, 1], 1.5)
point.setfillcolor(graphcolor)
point.fill()
point.draw()


def f(x):
    return math.asin(x)

graph = Graph(Function(f))
graph.setdomain([-0.99999, 0.99999])
graph.setcolor(magenta)
graph.draw()

point = Point([-1, -0.5*pi], 1.5)
point.setfillcolor(magenta)
point.fill()
point.draw()

point = Point([1, 0.5*pi], 1.5)
point.setfillcolor(magenta)
point.fill()
point.draw()

label = Label(r"$f$", [1, 0.8], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$f^{-1}$", [0.8, 1], alignment = "rb", offset = [-1, 1] )
label.draw()

label = Label(r"$(\frac{\pi}{2}, 1)$", [0.5*pi, 1], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$(1,\frac{\pi}{2})$", [1, 0.5*pi], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
