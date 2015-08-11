from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("1_5_PPprimeplot", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-2*margin,height-2*margin], 
                 [-10, -50, 90, 450])

xrange = [-10, 10, 90]
yrange = [-50, 50, 450]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks(xrange, yrange)
axes.drawticks()

axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0,20,80],[0,100,400])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label(r"$y = P(t)$", [10,350], alignment = "lt", offset = [0, -2] )
label.draw()

label = Label(r"$^\circ$F", [5,410], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"min", [80,20], alignment = "lb", offset = [2, 2] )
label.draw()


############# original function graph

def f(x):
    return 400-330*math.exp(-0.03*x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setdomain([0,90])
graph.setlinewidth(graphwidth)
graph.draw()

restore()

############## now the derivative function graph

save()
margin = 10

setupcoordinates([width+2*margin,margin,2*width-2*margin,height-2*margin], 
                 [-10, -2, 90, 18])

xrange = [-10, 10, 90]
yrange = [-2, 2, 18]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks(xrange, yrange)
axes.drawticks()

axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0,20,80], [0,4,16])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label(r"$y = P'(t)$", [10,10], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$^\circ$F/min", [5,16], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"min", [80,1], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 400-330*math.exp(-0.03*x)

derivative = Function(f).differentiate()
graph = Graph(derivative, color=darkgreen)
graph.setdomain([0,90])
graph.draw()

restore()

endfigure()
