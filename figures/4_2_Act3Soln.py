from figures import *
from defaults import *

width = standardwidth*1.5
height = standardheight

beginfigure("4_2_Act3Soln", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -2, 5.5, 2])

grid = Grid([-0.5,6,5.5], [-2,4,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([1,1,5], [-1,1,1])
axes.drawticks()

axes.sethlabels([1,1,5])
axes.drawhlabels()
axes.setvlabels([-1,1,1])
axes.drawvlabels()

f = Function(lambda x: 0.5*x**2 - 3*x + 3.5)

rs = RiemannSum(f, 5, #  g = Function(lambda x: x*x*x), 
                domain = [1,5], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()


label = Label(r"$y = v(t)$", [1,1], alignment = "lb", offset = [3,3])
label.draw()



restore()

endfigure()
