from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_1_Ex1", 2*width, height)

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

f = Function(lambda x : 0)

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([-1,0])
graph.draw()

f = Function(lambda x : x)

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([0,1])
graph.draw()

f = Function(lambda x : 3 - 2*x)

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([1,3])
graph.draw()

f = Function(lambda x : -3+3*(x-3))

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([3,5])
graph.draw()

f = Function(lambda x : 3 - 3*(x-5))

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([5,6])
graph.draw()

f = Function(lambda x : 0)

graph = Graph(f, color = tangentlinecolor, linewidth = graphwidth)
graph.setdomain([6,7])
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

axes.setlabels([0,2,4], # you can do this separately with seth(v)labels
               [-2,2,2])
axes.drawlabels()

f = Function(lambda x : 1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([-1,0])
graph.draw()

f = Function(lambda x : 1 + 0.5*x**2)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([0,1])
graph.draw()

f = Function(lambda x : -0.5 + 3*x - x**2)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([1,3])
graph.draw()

f = Function(lambda x : 8.5 - 3*x + 1.5*(x-3)**2)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([3,5])
graph.draw()

f = Function(lambda x : -15.5 + 3*x - 1.5*(x-5)**2)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([5,6])
graph.draw()

f = Function(lambda x : 1)

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([6,7])
graph.draw()

label = Label(r"$F$", [6,1], alignment = "lb", offset = [2, 4] )
label.draw()

##

f = Function(lambda x : 1+2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([-1,0])
graph.draw()

f = Function(lambda x : 1 + 0.5*x**2 +2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([0,1])
graph.draw()

f = Function(lambda x : -0.5 + 3*x - x**2 +2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([1,3])
graph.draw()

f = Function(lambda x : 8.5 - 3*x + 1.5*(x-3)**2+2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([3,5])
graph.draw()

f = Function(lambda x : -15.5 + 3*x - 1.5*(x-5)**2+2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([5,6])
graph.draw()

f = Function(lambda x : 1+2)

graph = Graph(f, color = red, linewidth = graphwidth)
graph.setdomain([6,7])
graph.draw()

label = Label(r"$G$", [6,3], alignment = "lb", offset = [2, 4] )
label.draw()

##

f = Function(lambda x : 1-2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([-1,0])
graph.draw()

f = Function(lambda x : 1 + 0.5*x**2 -2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([0,1])
graph.draw()

f = Function(lambda x : -0.5 + 3*x - x**2 -2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([1,3])
graph.draw()

f = Function(lambda x : 8.5 - 3*x + 1.5*(x-3)**2-2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([3,5])
graph.draw()

f = Function(lambda x : -15.5 + 3*x - 1.5*(x-5)**2-2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([5,6])
graph.draw()

f = Function(lambda x : 1-2)

graph = Graph(f, color = magenta, linewidth = graphwidth)
graph.setdomain([6,7])
graph.draw()

label = Label(r"$H$", [6,-1], alignment = "lb", offset = [2, 4] )
label.draw()

restore()

endfigure()
