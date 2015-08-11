from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_VelArea", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,3.5,3.5])

grid = Grid([-0.5,0.5,3.5], 
            [-0.5,0.5,3.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [1,2,3])
axes.drawlabels()

f = Function(lambda x:2)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1,1.5], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = 2)
graph.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [3,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$v(t) = 2$", [2,2], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$A_1$", [1.25,1], alignment = "cc", offset = [0, 0] )
label.draw()

restore()

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-0.5,-0.5,3.5,3.5])

grid = Grid([-0.5,0.5,3.5], 
            [-0.5,0.5,3.5], 
            color = lightlightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,3], # you can do this separately with seth(v)labels
               [1,2,3])
axes.drawlabels()

f = Function(lambda x:0.5*math.sin(2*x)+2.05)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1,1.5], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = 2)
graph.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [3,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2.25,2.45], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$A_2$", [1.25,1.25], alignment = "cc", offset = [0, 0] )
label.draw()

restore()


endfigure()
