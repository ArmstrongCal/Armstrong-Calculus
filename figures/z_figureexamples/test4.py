from figures import *

beginfigure("test4", 200, 200)

save()
setupcoordinates([10, 10, 190, 190],
                 [-1, -1, 1, 1])

grid = Grid([-1,0.25,1], [-1,0.25,1], color = lightlightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-1,0.25,1], [-1,0.25, 1])
axes.drawticks()

axes.sethlabelscale(0.8)
axes.setvlabelscale(0.8)

axes.setlabels([-1, 0.5, 1], [-1,0.5, 1])
axes.drawlabels()

a = 0.65
dx = 0.35

axes.sethticksize(10)
axes.sethticks([a, 1, a])
axes.drawhticks()

square = Function(lambda x:x*x)
graph = Graph(square, color = blue)
graph.draw()

tangent = Graph(square.tangentline(a), domain=[a-dx,a+dx], color = red)
tangent.draw()

label = Label("$x$", [0.90, 0.05])
label.draw()

label = Label("$y$", [0.05, 0.90])
label.draw()

label = Label("$y=x^2$", [0.40, 0.75], scale=1.2)
label.draw()

slope = square.derivative(a)
import math
label = Label("tangent line", [0.5, 0.07], color = red, 
              angle = math.atan(slope),
              scale = 0.8)
label.draw()

restore()
endfigure()
