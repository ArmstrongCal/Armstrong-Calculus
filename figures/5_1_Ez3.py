from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_1_Ez3", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1,-4,7,4])

grid = Grid([-1,1,7], 
            [-4,1,4], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,6]) # you can do this in one line with setticks([], [])
axes.setvticks([-3,1,3])
axes.drawticks()

axes.setlabels([1,2,5], # you can do this separately with seth(v)labels
               [-3,2,3])
axes.drawlabels()

f = Function(lambda x : 1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([-1,0])
graph.draw()

f = Function(lambda x : -x+1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([0,2])
graph.draw()

f = Function(lambda x : -1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

f = Function(lambda x : -1+1*(x-3))

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([3,5])
graph.draw()

f = Function(lambda x : 1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([5,7])
graph.draw()

label = Label(r"$f$", [5,3], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin,margin,2*width-margin,height-margin],  
                 [-1,-4,7,4])

grid = Grid([-1,1,7], 
            [-4,1,4], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,6]) # you can do this in one line with setticks([], [])
axes.setvticks([-3,1,3])
axes.drawticks()

axes.setlabels([1,2,5], # you can do this separately with seth(v)labels
               [-3,2,3])
axes.drawlabels()

restore()

endfigure()
