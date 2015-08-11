from figures import *
from defaults import *

width = standardwidth
height = standardheight*0.9

beginfigure("4_4_Ez2", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-4,-3,28,18])

grid = Grid([-4,2,28], 
            [-3,1.5,18], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,4,24]) # you can do this in one line with setticks([], [])
axes.setvticks([0,3,15])
axes.drawticks()

axes.setlabels([0,4,24], # you can do this separately with seth(v)labels
               [0,3,15])
axes.drawlabels()

f = Function(lambda x : -0.25*x**3 + 1.5*x**2 + 1)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,4])
graph.draw()

f = Function(lambda x : 9)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([4,12])
graph.draw()

f = Function(lambda x : 9 + 1.5*(x-12))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([12,16])
graph.draw()

f = Function(lambda x : 15)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([16,20])
graph.draw()

f = Function(lambda x : 15 - 2.25*(x-20))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([20,24])
graph.draw()

label = Label("m/min", [1,15], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("min", [24,1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = v(t)$", [20,15], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
