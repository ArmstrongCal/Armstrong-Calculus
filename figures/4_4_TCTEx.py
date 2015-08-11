from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_4_TCTEx", width, height)

save()
margin = 15
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1,-1,13,13])

grid = Grid([-1,1,13], 
            [-1,1,13], 
            color = lightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,2,12]) # you can do this in one line with setticks([], [])
axes.setvticks([0,2,12])
axes.drawticks()

axes.setlabels([0,2,12], # you can do this separately with seth(v)labels
               [0, 2, 12])
axes.drawlabels()

f = Function(lambda x: 0.0069*x**3 - 0.125*x**2 + 11.079)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[4,10])
area.fill()
area.draw()

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.setdomain([0,12])
graph.draw()

label = Label(r"gal/day", [0.5,12], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"days", [12.1,0.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = r(t)$", [8,7], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
