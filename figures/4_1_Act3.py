from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_Act3", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-4.5,8.5,4.5])

grid = Grid([-0.5,0.5,8.5], 
            [-4.5,0.5,4.5], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,8]) # you can do this in one line with setticks([], [])
axes.setvticks([-4,1,4])
axes.drawticks()

axes.setlabels([2,2,8], # you can do this separately with seth(v)labels
               [-4,2,4])
axes.drawlabels()

f = Function(lambda x : 2 - 2*x)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,2])
graph.draw()

f = Function(lambda x : -2)

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

f = Function(lambda x : -2 + 2*(x-3))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([3,6])
graph.draw()

f = Function(lambda x : 4 - 2*(x-6))

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([6,8])
graph.draw()

label = Label("m/sec", [0.25,4], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("sec", [8,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = v(t)$", [6.5,3], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

save()
margin = 10
setupcoordinates([margin+width,margin,2*width-margin,height-margin], 
                 [-0.5,-9,8.5,9])

grid = Grid([-0.5,0.5,8.5], 
            [-9,1,9], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,8]) # you can do this in one line with setticks([], [])
axes.setvticks([-8,2,8])
axes.drawticks()

axes.setlabels([2,2,8], # you can do this separately with seth(v)labels
               [-8,4,8])
axes.drawlabels()

f = Function(lambda x : 2*x - x**2 + 1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,2])
#graph.draw()

f = Function(lambda x : -2*(x-2)+1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
#graph.draw()

f = Function(lambda x : -2*(x-3)+(x-3)**2 - 1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([3,6])
#graph.draw()

f = Function(lambda x : 4*(x-6)-(x-6)**2 + 2)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([6,8])
#graph.draw()

label = Label(r"$y = s(t)$", [8,6], alignment = "rb", offset = [-2, 2] )
#label.draw()

restore()

endfigure()

