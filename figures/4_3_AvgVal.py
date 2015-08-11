from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_3_AvgVal", 3*width, height)

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

f = Function(lambda x: 0.5*(x-1)**2 + 1)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.5,3])
area.fill()
area.draw()

graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$\int_a^b f(x) \, dx$", [1.75,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y = f(x)$", [3.4,4], alignment = "rb", offset = [-2, 2] )
label.draw()


restore()

##############

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
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

f = Function(lambda x: 1.54167)

area = AreaBetweenCurves(f, fillcolor = lightgreen, domain=[0.5,3])
area.fill()
area.draw()

graph = Graph(f, color = darkgreen, linewidth = graphwidth)
graph.draw()

f = Function(lambda x: 0.5*(x-1)**2 + 1)
graph = Graph(f, color = lightblue, linewidth = 1)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$f_{\mbox{\tiny{AVG}}[a,b]}$", [0, 1.54], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$(b-a) \cdot f_{\mbox{\tiny{AVG}}[a,b]}$", [1.75, 0.5], alignment = "cc", offset = [0,0] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$y = f(x)$", [3.4,4], alignment = "rb", offset = [-2, 2] )
label.draw()
restore()

##################

save()
margin = 10
setupcoordinates([2*width+margin,margin,3*width-margin,height-margin], 
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

f = Function(lambda x: 0.5*(x-1)**2 + 1)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.5,3])
area.fill()
area.draw()

f = Function(lambda x: 1.54167)

area = AreaBetweenCurves(f, fillcolor = lightgreen, domain=[0.5,3])
area.fill()
area.draw()



f = Function(lambda x: 1.54167)

area = AreaBetweenCurves(f, fillcolor = lightgray, domain=[2.04084,3])
area.fill()

f = Function(lambda x: 0.5*(x-1)**2 + 1)

area = AreaBetweenCurves(f, fillcolor = lightgray, domain=[0.5,2.04084])
area.fill()

f = Function(lambda x: 1.54167)
area = AreaBetweenCurves(f, fillcolor = lightgreen, domain=[0.5,3])
area.draw()

graph = Graph(f, color = darkgreen, linewidth = graphwidth)
graph.draw()

f = Function(lambda x: 0.5*(x-1)**2 + 1)
graph = Graph(f, color = graphcolor, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.5,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$b$", [3,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$A_1$", [1.1,1.05], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$A_2$", [2.65,1.7], alignment = "cb", offset = [0, 2] )
label.draw()


label = Label(r"$y = f(x)$", [3.4,4], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
