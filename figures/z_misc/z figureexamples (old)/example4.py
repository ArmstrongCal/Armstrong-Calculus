from figures import *

width = 200
height = 200
beginfigure("example4", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], [-0.1,-0.1,1.1,1.1])

grid = Grid([-1,0.25, 1], [-1,0.25,1])
grid.setcolor(lightgray)
grid.draw()

grid = Grid([0, 1, 1], [0,1,1])
grid.setcolor(gray)
grid.draw()

axes = Axes()
axes.draw()

f = Function(lambda x:x*x)

rs = RiemannSum(f, 10)         # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.setdomain([0,1])
rs.setstyle(RiemannSum.LEFT)   # LEFT is default, MID and RIGHT are available
rs.setfillcolor(orange)
rs.fill()
rs.draw()

graph = Graph(f)
graph.setcolor(blue)
graph.setlinewidth(2)
graph.draw()



restore()
endfigure()
