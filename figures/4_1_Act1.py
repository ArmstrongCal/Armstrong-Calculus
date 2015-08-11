from figures import *
from defaults import *

width = 120
height = 160

beginfigure("4_1_Act1", width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,2.5,3.5])

grid = Grid([-0.5,0.25,2.5], 
            [-0.5,0.25,3.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,2], # you can do this separately with seth(v)labels
               [1,1,3])
axes.drawlabels()

f = Function(lambda x : 0.5*(x-1)**3+2)

rs = RiemannSum(f, 6, #  g = Function(lambda x: x*x*x), 
                domain = [0,3], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
#rs.fill()
#rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.25,2.25])
graph.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2,2.5], alignment = "rb", offset = [-2, 2] )
label.draw()


restore()


endfigure()
