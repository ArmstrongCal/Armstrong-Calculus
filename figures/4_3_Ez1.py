from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_3_Ez1", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-2.5,4.5,2.5])

grid = Grid([-0.5,0.5,4.5], 
            [-2.5,0.5,2.5], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2,1,2])
axes.drawticks()

axes.setlabels([1,1,4], # you can do this separately with seth(v)labels
               [-2,1,2])
axes.drawlabels()

f = Function(lambda x : 1 - 2*x)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,1.5])
graph.draw()

f = Function(lambda x : -2 + 1*(x-1.5))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([1.5,4])
graph.draw()

label = Label("ft/sec", [0.1,2], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("sec", [4,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = v(t)$", [4,-1], alignment = "rt", offset = [-2, -2] )
label.draw()

restore()

endfigure()
