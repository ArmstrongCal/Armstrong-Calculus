from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_Act3Soln", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-4.5,8.5,4.5])

grid = Grid([-0.5,0.5,8.5], 
            [-4.5,0.5,4.5], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,8]) # you can do this in one line with setticks([], [])
axes.setvticks([-4,1,4])
axes.drawticks()

axes.setlabels([2,2,8], # you can do this separately with seth(v)labels
               [-4,2,4])
axes.drawlabels()

f = Function(lambda x : 2 - 2*x)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[0,2])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,2])
graph.draw()

f = Function(lambda x : -2)

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[2,3])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

f = Function(lambda x : -2 + 2*(x-3))

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[3,5])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[5,6])
area.fill()
area.draw()


graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([3,6])
graph.draw()

f = Function(lambda x : 4 - 2*(x-6))

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[6,7])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = boxcolor, domain=[7,8])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([6,8])
graph.draw()

label = Label("m/sec", [0.25,4], alignment = "lb", offset = [2, 0] )
label.draw()

label = Label("sec", [8,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = v(t)$", [6.5,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$1$", [0.4, 0.5], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$1$", [4.6, 0.5], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$1$", [7.4, 0.5], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$1$", [1.6, -0.5], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$1$", [3.4, -0.5], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$2$", [2.5, -1], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$3$", [5.5, 2], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

label = Label(r"$3$", [6.5, 2], alignment = "cc", offset = [0,0], scale = 0.75 )
label.draw()

p1 = Point([1,0], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([2,-2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([3,-2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([4,0], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([5,2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([6,4], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([7,2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

save()
margin = 10
setupcoordinates([margin+width,margin,2*width-margin,height-margin], 
                 [-0.5,-9,8.5,9])

grid = Grid([-0.5,0.5,8.5], 
            [-9,1,9], 
            color = gridcolor, linewidth = gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,8]) # you can do this in one line with setticks([], [])
axes.setvticks([-8,2,8])
axes.drawticks()

axes.setlabels([2,2,8], # you can do this separately with seth(v)labels
               [-8,4,8])
axes.drawlabels()

f = Function(lambda x : 2*x - x**2 + 1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([0,2])
graph.draw()

f = Function(lambda x : -2*(x-2)+1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([2,3])
graph.draw()

f = Function(lambda x : -2*(x-3)+(x-3)**2 - 1)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([3,6])
graph.draw()

f = Function(lambda x : 4*(x-6)-(x-6)**2 + 2)
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([6,8])
graph.draw()

label = Label(r"$y = s(t)$", [8,6], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
