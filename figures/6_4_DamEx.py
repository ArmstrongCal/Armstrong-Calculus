from figures import *
from defaults import *

width = 1.5*standardwidth
height = standardheight
beginfigure("6_4_DamEx", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-60, -30, 60, 5])

grid = Grid([-60, 120, 60], [-30, 35, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-45, 90, 45]) # you can do this in one line with setticks([], [])
axes.setvticks([-25, 10, -15])
axes.drawticks()

axes.setlabels([0, 45, 45], # you can do this separately with seth(v)labels
               [0, 20, 10])
#axes.drawlabels()

p1 = [-45,0]
q1 = [45,0]
r1 = [30,-25]
s1 = [-30, -25]

points1 = [p1,q1,r1,s1]
trap1 = Polygon(points = points1, color = darkblue, fillcolor = gray, linewidth = 1.5, closed = True)
trap1.setmiterlimit(1)
trap1.draw()

line = Line([5,-5], [5,-15], color=red, linewidth = 0.5)
line.draw()

label = Label(r"$x-5$", [5,-10], alignment = "lc", offset = [3, 0], scale=0.8 )
label.draw()

line = Line([-42,-5], [42,-5], color=darkblue, linewidth = 1, dash=[2,2])
line.draw()

p2 = [36,-14]
q2 = [36,-16]
r2 = [-36,-16]
s2 = [-36,-14]

points2 = [p2,q2,r2,s2]
rect2 = Polygon(points = points2, color = red, fillcolor = gray, linewidth = 1.5, closed = True)
rect2.setmiterlimit(1)
rect2.draw()


label = Label(r"$\triangle x$", [36,-15], alignment = "lc", offset = [3, 0], scale=0.8 )
label.draw()

label = Label(r"$x$", [0,-15], alignment = "rc", offset = [-6, 0], scale=0.8 )
label.draw()


point = Point([30,-25], size = 1.5, fillcolor=pointcolor)
point.fill()
point.draw()

label = Label(r"$(25,30)$", [30,-25], alignment = "lt", offset = [2, -2] )
label.draw()

label = Label(r"$45$", [45,0.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y = f(x)$", [39,-10], alignment = "lc", offset = [2, 0] )
label.draw()

label = Label(r"$x^+$", [2,-28], alignment = "lc", offset = [2, 0] )
label.draw()

label = Label(r"$y^+$", [51,-0.5], alignment = "lt", offset = [2, -2] )
label.draw()



restore()

endfigure()
