from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("6_5_InfIntegrand", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.25,-0.5,1.25,3])

grid = Grid([-0.25,1.5,1.25], 
            [-0.5,3.5,3], 
            color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

f = Function(lambda x: 1/math.sqrt(x))

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.2,1])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.1,1.25])
cliptoboundingbox()
graph.draw()

label = Label("$y$", [-0.125,2.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$x$", [1.1,0.05], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$f(x) = \frac{1}{\sqrt{x}}$", [0.5,1.414], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$1$", [1,-0.3], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label("$a$", [0.2,-0.3], alignment = "cb", offset = [0, 2] )
label.draw()

restore()


save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                  [-0.25,-0.5,1.25,3])

f = Function(lambda x: 2.9999)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0,0.11111])
area.fill()
cliptoboundingbox()
area.draw()

f = Function(lambda x: 1/math.sqrt(x))

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.11111,1])
area.fill()
cliptoboundingbox()
area.draw()

line = Line([0.11111,0],[0.11111,3], color = lightblue, linewidth = 2)
line.draw()

line = Line([1,0],[1,1], color = black)
line.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0.1,1.25])
cliptoboundingbox()
graph.draw()

grid = Grid([-0.25,1.5,1.25], 
            [-0.5,3.5,3], 
            color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

label = Label("$y$", [-0.125,2.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$x$", [1.1,0.05], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$f(x) = \frac{1}{\sqrt{x}}$", [0.5,1.414], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("$1$", [1,-0.3], alignment = "cb", offset = [0, 2] )
label.draw()

restore()


endfigure()
