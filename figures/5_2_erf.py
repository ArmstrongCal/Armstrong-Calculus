from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_2_erf", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-3, -1.5, 3, 1.5])

xrange = [-3, 6, 3]
yrange = [-1.5,3,1.5]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,2]) 
axes.setvticks([-1,0.5,1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1,1,1])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([-2,2,2])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()


label = Label(r"$f(t)=e^{-t^2}$", [0,1], alignment = "lb", offset = [2, 2], scale = 0.8 )
label.draw()


### first original function graph

def f(x):
    return math.exp(-x**2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin, margin, 2*width-margin, height-margin], 
                  [-3, -1.5, 3, 1.5])

xrange = [-3, 6, 3]
yrange = [-1.5,3,1.5]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,2]) 
axes.setvticks([-1,0.5,1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1,1,1])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([-2,2,2])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()


label = Label(r"$E(x)=\int_0^x e^{-t^2} dt$", [0,1], alignment = "lb", offset = [2, 2], scale = 0.8 )
label.draw()



def f(x):
    return x - 0.3333*x**3 + 0.1*x**5 - 0.02381*x**7 + 0.0046296*x**9 - 0.0007576*x**11 + 0.00010684*x**13 - 0.0000132275*x**15 + 0.0000014589*x**17


graph = Graph(Function(f), color = graphcolor, linewidth = 1.5)
graph.setdomain([-1.75,1.75])
graph.draw()


def f(x):
    return 0.885

graph = Graph(Function(f), color = graphcolor, linewidth = 1.5)
graph.setdomain([1.75,3])
graph.draw()

def f(x):
    return -0.885

graph = Graph(Function(f), color = graphcolor, linewidth = 1.5)
graph.setdomain([-3,-1.75])
graph.draw()



restore()

endfigure()
