from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_4_UnitCircle", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.25, -1.25, 1.25, 1.25])

grid = Grid([-1.25, 0.25, 1.25], [-1.25, 0.25, 1.25])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 1])
axes.drawticks()

#axes.setlabels([-1, 1, 1], # you can do this separately with seth(v)labels
#               [-1, 1, 1])
#axes.sethlabelscale(scaleofaxeslabels)
#axes.setvlabelscale(scaleofaxeslabels)
#axes.drawlabels()

circle = Circle([0,0], 1, color = graphcolor)
circle.draw()

def f(x):
    return math.sqrt(3)*x

graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,0.5])
graph.draw()

linev = Line([0.5,0], [0.5,0.5*math.sqrt(3)], color = tangentlinecolor, linewidth = graphwidth)
lineh = Line([0,0], [0.5,0], color = tangentlinecolor, linewidth = graphwidth)
linev.draw()
lineh.draw()

p1 = Point([0.5,0.5*math.sqrt(3)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$1$", [0.25,0.5], alignment = "rb", offset = [-2, 2])
label.draw()

label = Label(r"$\theta$", [0.2,0.25], alignment = "lt", offset = [0, -1])
label.draw()

label = Label(r"$(x,y)$", [0.5,0.5*math.sqrt(3)], alignment = "lb", offset = [2, 2])
label.draw()

label = Label(r"$\sin(\theta)$", [0.54,0.3], alignment = "lb", offset = [1, 1])
label.draw()

label = Label(r"$\cos(\theta)$", [0.27,-0.25], alignment = "cb", offset = [2, -1])
label.draw()


restore()

endfigure()
