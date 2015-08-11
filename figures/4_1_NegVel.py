from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_NegVel", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -6, 3.5, 6])

grid = Grid([-0.5, 0.5, 3.5], [-6, 1.5, 6])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([-4.5,1.5,4.5])
axes.drawticks()

axes.setlabels([1,2,3], # you can do this separately with seth(v)labels
               [-4.5,1.5,4.5])
axes.drawlabels()

f = Function(lambda x : 3)

rs = RiemannSum(f, 1, 
                domain = [0,1.5], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,1.5])
graph.draw()


f = Function(lambda x : -4)

rs = RiemannSum(f, 1, 
                domain = [1.5,2], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([1.5,2])
graph.draw()

f = Function(lambda x : 3)

rs = RiemannSum(f, 1, 
                domain = [2,3], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
rs.fill()
rs.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

p1 = Point([1.5,3], 1.5)
p1.setfillcolor(emptypoint)
#p1.fill()
#p1.draw()

p1 = Point([1.5,-4], 1.5)
p1.setfillcolor(emptypoint)
#p1.fill()
#p1.draw()

p1 = Point([2,-4], 1.5)
p1.setfillcolor(emptypoint)
#p1.fill()
#p1.draw()

p1 = Point([2,3], 1.5)
p1.setfillcolor(emptypoint)
#p1.fill()
#p1.draw()

label = Label("mph", [0.1,5], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("hrs", [3,0.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$A_1 = 4.5$", [0.75, 1.5], alignment = "cc", offset = [0,0], scale = 0.75)
label.draw()

label = Label(r"$A_2 = 2$", [1.75, -2], alignment = "cc", offset = [5,0], scale = 0.75)
label.draw()

label = Label(r"$A_3 = 3$", [2.5, 1.5], alignment = "cc", offset = [0,0], scale = 0.75)
label.draw()

label = Label(r"$y=v(t)$", [1.5,3], alignment = "rb", offset = [-2, 2], scale = 0.75 )
label.draw()


restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.5, -6, 3.5, 6])

grid = Grid([-0.5, 0.5, 3.5], [-6, 1.5, 6])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([-4.5,1.5,4.5])
axes.drawticks()

axes.setlabels([1,2,3], # you can do this separately with seth(v)labels
               [-4.5,1.5,4.5])
axes.drawlabels()


def f(x):
    return 3*x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1.5])
graph.draw()

def f(x):
    return 4.5-4*(x-1.5)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,2])
graph.draw()

def f(x):
    return 2.5+3*(x-2)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3])
graph.draw()

label = Label("miles", [0.1,5], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("hrs", [3,0.5], alignment = "lb", offset = [2, 2] )
label.draw()

p1 = Point([1.5,4.5], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label("$(1.5,4.5)$", [1.5,4.5], alignment = "lb", offset = [2, 2], scale = 0.75 )
label.draw()

p1 = Point([2,2.5], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label("$(2,2.5)$", [2,2.5], alignment = "lt", offset = [2, -2], scale = 0.75 )
label.draw()

p1 = Point([3,5.5], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label("$(3,5.5)$", [3,5.5], alignment = "lb", offset = [2, 2], scale = 0.75 )
label.draw()

label = Label(r"$y=s(t)$", [1,3], alignment = "rb", offset = [-2, 2], scale = 0.75 )
label.draw()

restore()

endfigure()
