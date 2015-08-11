from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_Act2", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-36,2.5,36])

grid = Grid([-0.5,0.5,2.5], 
            [-36,12,36], 
            color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([-24,12,24])
axes.drawticks()

axes.setlabels([1,1,2], # you can do this separately with seth(v)labels
               [-24,12,24])
axes.drawlabels()

f = Function(lambda x : 32 - 32*x)

rs = RiemannSum(f, 6, #  g = Function(lambda x: x*x*x), 
                domain = [0,3], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
#rs.fill()
#rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,2])
graph.draw()

label = Label("ft/sec", [0.1,32], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("sec", [2,2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$v(t)=32-32t$", [0.625, 12], alignment = "lb", offset = [2, 2] )
label.draw()


restore()


endfigure()
