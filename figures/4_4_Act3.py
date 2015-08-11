from figures import *
from defaults import *

width = standardwidth*2
height = standardheight

beginfigure("4_4_Act3", width, height)

save()
margin = 15
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-5,-2.5,35,17.5])

grid = Grid([-5,2.5,35], 
            [-2.5,2.5,17.5], 
            color = lightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,5,30]) # you can do this in one line with setticks([], [])
axes.setvticks([0,5,15])
axes.drawticks()

axes.setlabels([0,10,30], # you can do this separately with seth(v)labels
               [0,5,15])
axes.drawlabels()

f = Function(lambda x: -0.05*x**2 + x + 10)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([0,10])
graph.draw()

f = Function(lambda x: 15)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([10,20])
graph.draw()

f = Function(lambda x: -0.05*x**2 + 2*x - 5)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([20,30])
graph.draw()

label = Label(r"cal/min", [1,15], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"min", [30,1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = c(t)$", [25,13.5], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
