from figures import *
from defaults import*

width = standardwidth
height = standardheight*1.5
beginfigure("4_4_TCT", 2*width, height)

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

axes.setlabels([0, 1, 2], [-4,1,4])
axes.drawlabels()

label = Label(r"$y = f'(x)$", [1.3,-3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$3$", [3,0.2], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$4$", [4,0.2], alignment = "cb", offset = [0, 2] )
label.draw()


f = Function(lambda x : 4 - 2*x)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[0,1])
area.fill()
area.draw()

label = Label(r"$3$", [0.5,1.5], alignment = "cc", offset = [0, 0] )
label.draw()

f = Function(lambda x : 4 - 2*x)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[1,2])
area.fill()
area.draw()

label = Label(r"$1$", [1.35,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

f = Function(lambda x : 4 - 2*x)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[2,3])
area.fill()
area.draw()

label = Label(r"$1$", [2.65,-0.5], alignment = "cc", offset = [0, 0] )
label.draw()

f = Function(lambda x : 4 - 2*x)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[3,4])
area.fill()
area.draw()

label = Label(r"$3$", [3.5,-1.5], alignment = "cc", offset = [0, 0] )
label.draw()

def f(x):
    return 4-2*x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.draw()

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
axes.sethlabelscale(scaleofaxeshlabels)
axes.setvlabelscale(scaleofaxesvlabels)
axes.drawlabels()


label = Label(r"$y = f(x)$", [2.6,-3], alignment = "lb", offset = [2, 2] )
label.draw()



############# original function graph

def f(x):
    return 4*x-x*x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.draw()


a=0
point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(0,0)$", [0,0], alignment = "lb", offset = [2, 2] )
label.draw()

a=1
point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(1,3)$", [1,3], alignment = "lt", offset = [2, -2] )
label.draw()

a=2
point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(2,4)$", [2,4], alignment = "lb", offset = [2, 2] )
label.draw()

a=3
point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(3,3)$", [3,3], alignment = "lb", offset = [2, 2] )
label.draw()

a=4
point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$(4,0)$", [4,0], alignment = "lb", offset = [1,2] )
label.draw()

restore()

endfigure()
