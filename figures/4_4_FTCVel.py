from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_4_FTCVel", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,3.5,4.5])

grid = Grid([-0.5,4,3.5], 
            [-0.5,5,4.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
#axes.drawticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [1,2,3])
#axes.drawlabels()

f = Function(lambda x: -0.25*(x-1)**2 + 3)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.5,3])
area.fill()
area.draw()

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$D =\int_a^b v(t) \, dt$", [1.7,1.5], alignment = "cc", offset = [0, 0] )
label.draw()
label = Label(r"$=s(b)-s(a)$", [1.86,0.9], alignment = "cc", offset = [4, 0] )
label.draw()

label = Label(r"$y = v(t)$", [3.4,2.7], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
