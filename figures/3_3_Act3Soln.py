from figures import *
from defaults import*

width = 200
height = 150
beginfigure("3_3_Act3Soln", width, height)

save()
margin = 7
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [-3,-2,17,13])

box = Box([0,0,15,10], color = black)
box.draw()

p = [0,0]
q = [0,2]
r = [2,2]
s = [2,0]

points = [p,q,r,s]
square = Polygon(points = points, color = gray, fillcolor = gray, linewidth = 1, closed = True)
square.fill()
square.draw()

label = Label(r"$x$", [1, 2], alignment = "cb", offset = [0, 2])
label.draw()
label = Label(r"$x$", [2, 1], alignment = "lc", offset = [2, 0])
label.draw()

p = [0,8]
q = [2,8]
r = [2,10]
s = [0,10]

points = [p,q,r,s]
square = Polygon(points = points, color = gray, fillcolor = gray, linewidth = 1, closed = True)
square.fill()
square.draw()

p = [13,8]
q = [15,8]
r = [15,10]
s = [13,10]

points = [p,q,r,s]
square = Polygon(points = points, color = gray, fillcolor = gray, linewidth = 1, closed = True)
square.fill()
square.draw()

p = [13,0]
q = [15,0]
r = [15,2]
s = [13,2]

points = [p,q,r,s]
square = Polygon(points = points, color = gray, fillcolor = gray, linewidth = 1, closed = True)
square.fill()
square.draw()


label = Label(r"$10-2x$", [0, 5], alignment = "rc", offset = [-2, 0])
label.draw()
label = Label(r"$15-2x$", [7.5, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

restore()
endfigure()
