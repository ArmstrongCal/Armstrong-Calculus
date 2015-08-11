from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_5_InfReg", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.2,5.5,0.5])

grid = Grid([-0.5,6,5.5], 
            [-0.2,0.7,0.5], 
            color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

f = Function(lambda x: 0.3*math.exp(-0.3*x))

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0,3.5])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.5,5.5])
cliptoboundingbox()
graph.draw()

label = Label("$y$", [0.1,0.4], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$t$", [5,-0.05], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$b$", [3.5,-0.075], alignment = "cb", offset = [0, 2] )
label.draw()

restore()


save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-0.5,-0.2,5.5,0.5])

grid = Grid([-0.5,6,5.5], 
            [-0.2,0.7,0.5], 
            color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

f = Function(lambda x: 0.3*math.exp(-0.3*x))

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0,5.7])
cliptoboundingbox()
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.5,5.5])
cliptoboundingbox()
graph.draw()

label = Label("$y$", [0.1,0.4], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$t$", [5,-0.075], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$\cdots$", [5,0.05], alignment = "ct", offset = [0,0] )
label.draw()



restore()


endfigure()
