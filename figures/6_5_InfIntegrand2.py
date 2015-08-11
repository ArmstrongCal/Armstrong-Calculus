from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_5_InfIntegrand2", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,4.5,4.5])

f = Function(lambda x: 4.49999)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[1.5286,2])
area.fill()
cliptoboundingbox()
area.draw()

f = Function(lambda x: 1/(x-2)**2)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[1,1.5286])
area.fill()
cliptoboundingbox()
area.draw()

line = Line([1.5286,0],[1.5286,4.5], color = lightblue, linewidth = 2)
line.draw()

line = Line([1,0],[1,1], color = black)
line.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.5,1.75])
cliptoboundingbox()
graph.draw()

f = Function(lambda x: 4.49999)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[2, 2.4714])
area.fill()
cliptoboundingbox()
area.draw()

f = Function(lambda x: 1/(x-2)**2)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[2.4714,3])
area.fill()
cliptoboundingbox()
area.draw()

line = Line([2.4714,0],[2.4714,4.5], color = lightblue, linewidth = 2)
line.draw()

line = Line([3,0],[3,1], color = black)
line.draw()

line = Line([2,0],[2,4.5], color = black, dash = [8, 2])
line.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2.25,4.5])
cliptoboundingbox()
graph.draw()

grid = Grid([-0.5,5,4.5], 
            [-0.5,5,4.5], 
            color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1,1,3]) # you can do this in one line with setticks([], 
axes.drawhticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [0,10,4])
axes.drawlabels()

label = Label("$y$", [0.125,4], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$x$", [4,-0.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = \frac{1}{(x-2)^2}$", [2.7,1.8], alignment = "lb", offset = [2, 2] )
label.draw()


restore()

endfigure()
