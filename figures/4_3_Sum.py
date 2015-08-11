from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_3_Sum", 3*width, height)

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

f = Function(lambda x:0.5*math.sin(2*x)+1.25)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.2,2.8])
area.fill()
area.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1,1.6], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.2,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$x_i$", [1,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$A = f(x_i) \triangle x$", [1.3,2.1], alignment = "cc", offset = [0, 0])
label.draw()

label = Label(r"$A$", [1.3,0.85], alignment = "cc", offset = [0, 0])
label.draw()

label = Label("$x_{i+1}$", [1.6,-0.4], alignment = "cb", offset = [2, -2] )
label.draw()

label = Label("$b$", [2.8,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$f$", [3.4,1.6], alignment = "rb", offset = [-2, 2] )
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

f = Function(lambda x:1.5*math.exp(-x) + 0.5)

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[0.2,2.8])
area.fill()
area.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1,1.6], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.2,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$x_i$", [1,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$B = g(x_i) \triangle x$", [1.3,1.7], alignment = "cc", offset = [0, 0])
label.draw()

label = Label(r"$B$", [1.3,0.45], alignment = "cc", offset = [0, 0])
label.draw()

label = Label("$x_{i+1}$", [1.6,-0.4], alignment = "cb", offset = [2, -2] )
label.draw()

label = Label("$b$", [2.8,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$g$", [3.4,0.6], alignment = "rb", offset = [-2, 2] )
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

f = Function(lambda x:1.5*math.exp(-x) + 0.5 + 0.5*math.sin(2*x)+1.25)

area = AreaBetweenCurves(f, fillcolor = lightgray, domain=[0.2,2.8])
area.fill()
area.draw()

rs = RiemannSum(f, 1, #  g = Function(lambda x: x*x*x), 
                domain = [1,1.6], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label("$a$", [0.2,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$x_i$", [1,-0.5], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$C = (f(x_i) + g(x_i)) \triangle x$", [1.6,3.5], alignment = "cc", offset = [0, 0])
label.draw()

label = Label(r"$C$", [1.3,1.5], alignment = "cc", offset = [0, 0])
label.draw()

label = Label("$x_{i+1}$", [1.6,-0.4], alignment = "cb", offset = [2, -2] )
label.draw()

label = Label("$b$", [2.8,-0.45], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$f+g$", [3.4,2.1], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
