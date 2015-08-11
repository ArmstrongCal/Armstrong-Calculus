from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_3_Act3Soln", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,4.5,4.5])

grid = Grid([-0.5,5,4.5], 
            [-0.5,5,4.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,4]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,4])
axes.drawticks()

axes.setlabels([0,2,4], # you can do this separately with seth(v)labels
               [0,2,4])
axes.drawlabels()

f = Function(lambda x: math.sqrt(4 - (x-2)**2))

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.001,3.999])
area.fill()
area.draw()

f = Function(lambda x: math.pi/2)

area = AreaBetweenCurves(f, fillcolor = lightgreen, domain=[0,4])
area.fill()
area.draw()

#[0.762018,3.23798]

graph = Graph(f, color = darkgreen, linewidth = graphwidth)
graph.draw()

f = Function(lambda x: math.sqrt(4 - (x-2)**2))
graph = Graph(f, color = graphcolor, linewidth = graphwidth, domain=[0.001,3.999])
graph.draw()

label = Label(r"$y = v(t)$", [3,2], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
