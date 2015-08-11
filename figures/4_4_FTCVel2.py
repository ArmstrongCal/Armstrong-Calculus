from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_4_FTCVel2", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1,-20,6,150])

grid = Grid([-1,7,6], 
            [-20,170,150], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,5]) # you can do this in one line with setticks([], [])
axes.setvticks([0,20,140])
axes.drawticks()

axes.setlabels([1,2,5], # you can do this separately with seth(v)labels
               [0, 20, 140])
axes.drawlabels()

f = Function(lambda x: 3*x**2 + 40)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[1,5])
area.fill()
area.draw()

cliptoboundingbox()
graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.draw()


label = Label(r"$D =\int_1^5 v(t) \, dt$", [3,35], alignment = "cc", offset = [0, 0] )
label.draw()
label = Label(r"$=284$", [2.65,15], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y = v(t)$", [5,112], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
