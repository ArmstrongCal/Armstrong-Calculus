from figures import *

width = 200
height = 200
beginfigure("example6", 2*width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-3*margin], 
                 [-3, -3, 3, 3])

grid = Grid([-3, 0.5, 3], [-3, 0.5, 3])
grid.setcolor(lightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-3, 1, 3], [-3, 1, 3])
axes.drawticks()

# we're going to clip so the graph doesn't go out of the box,
#   but first we'll save the unclipped state
save()
cliptoboundingbox()
points = [[-2, 2], [-1, 1], [0, -1], [1, 0], [2,1]]
lagrange = Lagrange(points)
# you can also add these with lagrange.addpoint(p)
# you must run setup to compute the coefficients of the polynomial
lagrange.setup()
graph = Graph(lagrange)
graph.setcolor(blue)
graph.draw()
# now restore the unclipped state
restore()

for p in points:
    point = Point(p, 3)
    point.setfillcolor(lightred)
    point.fill()
    point.draw()

label = Label("Lagrange", [-3, 3])
label.setoffset([0, 2])
label.draw()

restore()

save()
margin = 5
setupcoordinates([width+margin,margin,2*width-margin,height-3*margin], 
                 [-3, -3, 3, 3])

grid = Grid([-3, 0.5, 3], [-3, 0.5, 3])
grid.setcolor(lightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-3, 1, 3], [-3, 1, 3])
axes.drawticks()

save()
cliptoboundingbox()
points = [[-2, 2, 1], [0, -1, 0], [1.5, 0, 1]]
hermite = Hermite(points)
hermite.setup()
graph = Graph(hermite)
graph.setcolor(blue)
graph.draw()
restore()

dx = 0.5
for p in points:
    f = Function(lambda x: p[1] + p[2]*(x-p[0]))
    tangent = Graph(f)
    tangent.setdomain([p[0]-dx, p[0]+dx])
    tangent.setcolor(red)
    tangent.draw()

    point = Point(p, 3)
    point.setfillcolor(lightred)
    point.fill()
    point.draw()

label = Label("Hermite", [-3, 3])
label.setoffset([0, 2])
label.draw()

restore()

endfigure()
