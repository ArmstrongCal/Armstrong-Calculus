from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_3_VelArea", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
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
#axes.drawlabels()

f = Function(lambda x:0.5*math.sin(2*x)+2.05)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1.2,1.6], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = 1.5)
cliptoboundingbox()
graph.draw()

label = Label("ft/sec", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("sec", [3,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2.25,2.45], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$v(t)$", [1.2,1.15], alignment = "rc", offset = [-3, 0] )
label.draw()

label = Label(r"$\triangle t$", [1.4,-0.3], alignment = "cc", offset = [0, 0] )
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
#axes.drawlabels()

f = Function(lambda x: 1 + 0.3*x**2)

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1.2,1.6], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = 1.5)
cliptoboundingbox()
graph.draw()

label = Label("$y$", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$x$", [3,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= f(x)$", [2.25,2.25], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$f(x)$", [1.2,0.65], alignment = "rc", offset = [-3, 0] )
label.draw()

label = Label(r"$\triangle x$", [1.4,-0.3], alignment = "cc", offset = [0, 0] )
label.draw()


restore()


endfigure()
