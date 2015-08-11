from figures import *
from defaults import*

width = standardwidth
height = standardheight*1.5
beginfigure("1_4_ffprimeplot", 2*width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-2*margin,height-2*margin], 
                 [-1, -5, 5, 5])

xrange = [-1, 1, 5]
yrange = [-5, 1, 5]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0, 1, 4], [-4,1,4])
axes.drawticks()

axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0, 1, 4], [-4,1,4])
axes.sethlabelscale(scaleofaxeshlabels)
axes.setvlabelscale(scaleofaxesvlabels)
axes.drawlabels()

label = Label(r"$m=-4$", [4.1,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = f(x)$", [2.3,-3], alignment = "lb", offset = [2, 2] )
label.draw()



############# original function graph

def f(x):
    return 4*x-x*x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.draw()

a = 0
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(green)
tangent.draw()

point = Point([0, f(0)], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"$m=4$", [0.1,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

a = 1
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(cyan)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"$m=2$", [1.1,3.1], alignment = "lb", offset = [4, 2] )
label.draw()

a = 2
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(orange)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"$m=0$", [2,4.1], alignment = "cb", offset = [2, 2] )
label.draw()

a = 3
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(red)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"$m=-2$", [3.1,3.1], alignment = "lb", offset = [0, 2] )
label.draw()

a = 4
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(darkgreen)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

restore()

############## now the derivative function graph

save()
margin = 5
setupcoordinates([width+2*margin,margin,2*width-margin,height-2*margin], 
                 [-1, -5, 5, 5])

xrange = [-1, 1, 5]
yrange = [-5, 1, 5]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0, 1, 4], [-4,1,4])
axes.drawticks()

axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0, 1, 4], [-4,1,4])
axes.drawlabels()

label = Label(r"$y = f'(x)$", [1.2,-3], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 4-2*x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.draw()

a=0
point = Point([a, f(a)], 2)
point.setfillcolor(green)
point.fill()
point.draw()

label = Label(r"$(0,4)$", [0.1,4.1], alignment = "lb", offset = [2, 2] )
label.draw()

a=1
point = Point([a, f(a)], 2)
point.setfillcolor(cyan)
point.fill()
point.draw()

label = Label(r"$(1,2)$", [1.1,2.1], alignment = "lb", offset = [2, 2] )
label.draw()

a=2
point = Point([a, f(a)], 2)
point.setfillcolor(orange)
point.fill()
point.draw()

label = Label(r"$(2,0)$", [2.1,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

a=3
point = Point([a, f(a)], 2)
point.setfillcolor(red)
point.fill()
point.draw()

label = Label(r"$(3,-2)$", [3.1,-1.9], alignment = "lb", offset = [2, 2] )
label.draw()

a=4
point = Point([a, f(a)], 2)
point.setfillcolor(darkgreen)
point.fill()
point.draw()

label = Label(r"$(4,-4)$", [3.9,-4.1], alignment = "rt", offset = [-2, -2] )
label.draw()

restore()

endfigure()
