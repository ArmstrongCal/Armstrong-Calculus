from figures import *    # you'll always needs this

width = 200
height = 200
beginfigure("example1", width, height)

save()                   # saves the current coordinate system--just do it
margin = 5
setupcoordinates( [margin, margin, width-margin, height-margin],
                  [-2, -2, 2, 2])

grid = Grid([-2,0.5,2],  # initial x, x spacing, final x
            [-2,0.5,2], color = lightgray)  # initial y, y spacing, final y
grid.draw()

axes = Axes()
axes.setlinewidth(1)     # default is 1
axes.setcolor(black)     # black is the default
axes.draw()

axes.sethticks([-2,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([-2,1,2])
axes.drawticks()

axes.setlabels([-2,1,2], # you can do this separately with seth(v)labels
               [-2,1,2])
axes.sethlabelscale(0.8)
axes.setvlabelscale(0.8)
axes.drawlabels()

label = Label("$x$", [1.8, 0.1])
label.draw()

label = Label("$y$", [0.1, 1.8])
label.draw()

label = Label("$f$", [-1, 1.5])
label.setscale(1.2)
label.draw()

label = Label("$f'$", [1.5, 1.5])
label.setscale(1.2)
label.draw()

cliptoboundingbox()      # doesn't display stuff that spills out of box
function = Function(lambda x: x**2 - x - 1)
graph = Graph(function, color = blue, linewidth = 1.5)
#graph.setdomain([ ?, ?]) default is the entire window
#graph.setN(500)          default is 100 points
graph.draw()

derivative = function.differentiate()
graph = Graph(derivative, color=green)
graph.draw()

a = 1
dx = 0.8
tangentline = function.tangentline(a)
tangent = Graph(tangentline, domain = [a-dx, a+dx], color = red)
tangent.draw()

point = Point([a, derivative.value(a)], fillcolor = red)
point.fill()
point.draw()

restore()                 # restores the original coordinates--just do it
endfigure()               # writes everything out--you always need this
