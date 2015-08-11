from figures import *

def makefigure(gridsize):
    
    box = Box("boundingbox", fillcolor = white)
    # default box is the current bounding box
    box.fill()

    grid = Grid([-3, gridsize, 3], [-3, gridsize, 3], lightgray)
    grid.draw()

    axes = Axes()
    axes.draw()

    axes.setticks([-3, 1, 3], [-3, 1, 3])
    axes.drawticks()

    # we're going to clip so the graph doesn't go out of the box,
    #   but first we'll save the unclipped state
    save()
    cliptoboundingbox()
    graph = Graph(hermite, color = blue)
    graph.draw()

    point = Point([a, y], 3, fillcolor = lightred)
    point.fill()
    point.draw()

    # now restore the unclipped state
    restore()


points = [[-2, 2,1], [0, -1, 0], [1.5, 0, 0]]
hermite = Hermite(points)
hermite.setup()
width = 200
height = 200
beginfigure("example7", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
             [-3, -3, 3, 3])
a = -1.2
y = hermite.value(a)
dx = 0.25

makefigure(0.5)

outline = Box([a-dx, y-dx, 2*dx, 2*dx])
                   # arguments are lower left corner, width and heigh
outline.draw()

save()
setupcoordinates([0.3, 0.3, 2.7, 2.7], [a-dx, y-dx, a+dx, y+dx])
cliptoboundingbox()
makefigure(0.1)
restore()

box = Box([0.3, 0.3, 2.4, 2.4], color = gray)
box.draw()

restore()

endfigure()
