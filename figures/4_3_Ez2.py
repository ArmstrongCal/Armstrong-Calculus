from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_3_Ez2", 2*width, height)

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

f = Function(lambda x : 2*x)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,1])
graph.draw()

f = Function(lambda x : 2 - 4*(x-1))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([1,2])
graph.draw()

f = Function(lambda x : -2)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

f = Function(lambda x : -2 + 2*(x-3))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([3,4])
graph.draw()

label = Label(r"$y = f(x)$", [1.25,2], alignment = "lt", offset = [2, -2] )
label.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin,margin,2*width-margin,height-margin],  
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

f = Function(lambda x : -1*math.sqrt(1-(x-1)**2))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.001,1])
graph.draw()

f = Function(lambda x : -1+3*(x-1))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([1,2])
graph.draw()

f = Function(lambda x : math.sqrt(4-(x-2)**2))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3.999])
graph.draw()

label = Label(r"$y = g(x)$", [2,2], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
