from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_2_Ez1", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1.25,-4.5,6.75,6.5])

grid = Grid([-1.25,8,6.75], 
            [-4.5,11,6.5], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1,0.5,6.5]) # you can do this in one line with setticks([], [])
axes.setvticks([-4,1,6])
axes.drawticks()

axes.setlabels([1,1,6], # you can do this separately with seth(v)labels
               [-4,2,6])
axes.drawlabels()

f = Function(lambda x: -(0.05*(x+1))*(x-0.5)*(x-4)*(x-5)*(x-6.5) )

area = AreaBetweenCurves(f, fillcolor = lightlightgray, domain=[-1,0.5])
area.fill()
area.draw()

label = Label(r"$A_1$", [-0.3,-0.8], alignment = "cc", offset = [0, 0] )
label.draw()

f = Function(lambda x: -(0.05*(x+1))*(x-0.5)*(x-4)*(x-5)*(x-6.5) )

area = AreaBetweenCurves(f, fillcolor = lightgray, domain=[0.5,4])
area.fill()
area.draw()

label = Label(r"$A_2$", [2,3], alignment = "cc", offset = [0, 0] )
label.draw()


f = Function(lambda x: -(0.05*(x+1))*(x-0.5)*(x-4)*(x-5)*(x-6.5) )

area = AreaBetweenCurves(f, fillcolor = lightlightgray, domain=[4,5])
area.fill()
area.draw()


label = Label(r"$A_3$", [5,-2], alignment = "lt", offset = [2, -2] )
label.draw()

line = Line([5,-2], [4.5,-0.25], color = black, linewidth = 1)
line.draw()

f = Function(lambda x: -(0.05*(x+1))*(x-0.5)*(x-4)*(x-5)*(x-6.5) )

area = AreaBetweenCurves(f, fillcolor = lightgray, domain=[5,6.5])
area.fill()
area.draw()

label = Label(r"$A_4$", [5.95,0.8], alignment = "cc", offset = [0, 0] )
label.draw()


label = Label(r"$y = g(t)$", [3,4.25], alignment = "lt", offset = [2, -2] )
label.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin,margin,2*width-margin,height-margin],  
                 [-1.25,-11,6.75,16])

grid = Grid([-1.25,8,6.75], 
            [-11,27,16], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1,0.5,6.5]) # you can do this in one line with setticks([], [])
axes.setvticks([-10,2.5,15])
axes.drawticks()

axes.sethlabels([-1,1,6])
axes.drawhlabels()
axes.setvlabels([-10,5,15])
axes.drawvlabels()

restore()

endfigure()
