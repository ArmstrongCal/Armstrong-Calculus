from figures import *
from defaults import*

width = 200
height = 100
beginfigure("3_3_Ex1", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,1,10,6])

line = Line([1,5.5],[6,5.5], color=blue, linewidth = graphwidth)
line.draw()

label = Label(r"$x$", [3.5, 5], alignment = "cb", offset = [0, -2])
label.draw()

line = Line([6,5.4],[6,5.6], color=black, linewidth = graphwidth)
line.draw()

line = Line([6,5.5],[9,5.5], color=darkgreen, linewidth = graphwidth)
line.draw()

label = Label(r"$20-x$", [7.5, 5], alignment = "cb", offset = [0, -2])
label.draw()


p = [2,2]
q = [4,2]
r = [3,2+math.sqrt(3)]

points = [p,q,r]
triangle = Polygon(points = points, color = graphcolor, linewidth = 2, closed = True)
#triangle.fill()
triangle.draw()

label = Label(r"$\frac{x}{3}$", [3, 1.8], alignment = "ct", offset = [0, 0])
label.draw()

p = [7,2]
q = [8,2]
r = [8,3]
s = [7,3]

points = [p,q,r,s]
square = Polygon(points = points, color = darkgreen, linewidth = 2, closed = True)
square.draw()

label = Label(r"$\frac{20-x}{4}$", [7.5, 1.8], alignment = "ct", offset = [0, 0])
label.draw()

restore()
endfigure()
