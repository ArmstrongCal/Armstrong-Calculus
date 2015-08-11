from figures import *
from defaults import *

width = 180
height = 180
beginfigure("1_8_TanLine", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

##grid = Grid([-1, 1, 5], [-1, 1, 5])
##grid.setcolor(gridcolor)
##grid.setlinewidth(gridwidth)
##grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([2.2, 2, 3.5]) # you can do this in one line with setticks([], [])
axes.setvticks([2, 4, 5])
axes.setvticksize(1)
axes.drawticks()
axes.sethticksize(10)



##axes.setlabels([-1, 1, 5], # you can do this separately with seth(v)labels
##               [-1, 1, 5])
##axes.sethlabelscale(0.8)
##axes.setvlabelscale(0.8)
##axes.drawlabels()
label = Label("$x$", [4.5, -0.5])
label.draw()

label = Label(r"$y$", [0.3, 4.5])
label.draw()

label = Label(r"$y = f(x)$", [2.5,4], alignment = "lb", offset = [-2, 2]  )
label.draw()

label = Label(r"$a$", [2.1, -0.5])
label.draw()

label = Label(r"$(a,f(a))$", [2.2,1.5], alignment = "rb", offset = [-2, 2]  )
label.draw()

label = Label(r"$y = f'(a)(x-a) + f(a)$", [1.2,0.4], alignment = "lb", offset = [2, 2]  )
label.draw()


def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 2.2
dx = 1.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([2.2, f(2.2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

box = Box([2.0, f(2.2)-0.2, 0.4, 0.4], color = gridcolor)
box.draw()

restore()
save()

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [2.0,1.065,2.4,1.465])

outline = Box([2.0,1.065,0.4,0.4], color=gridcolor) # arguments are lower left corner, width and heigh
outline.draw()

label = Label(r"$(a,f(a))$", [2.2,1.27], alignment = "rb", offset = [-2, -2]  )
label.draw()

label = Label(r"$y = f(x)$", [2.25,1.33], alignment = "lb", offset = [-2, 2]  )
label.draw()

label = Label(r"$y = L(x)$", [2.05,1.165], alignment = "lb", offset = [-2, 2]  )
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.draw()

a = 2.2
dx = 1.4
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
##tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([2.2, f(2.2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()


endfigure()
