from figures import *
from defaults import*

width = 180
height = 120
beginfigure("3_4_PA1", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,5,3])

line = Line([0,0], [3,1], linewidth = 1, dash = [4,4], color = gray)
line.draw()

line = Line([3,3], [3,1], linewidth = 1, dash = [4,4], color = gray)
line.draw()

line = Line([5,1], [3,1], linewidth = 1, dash = [4,4], color = gray)
line.draw()

box = Box([0,0,2,2], color = black)
box.draw()

p = [2,0]
q = [5,1]
r = [5,3]
s = [2,2]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = gray, linewidth = 1, closed = True)
pgram.setmiterlimit(1)
pgram.draw()

p = [0,2]
q = [2,2]
r = [5,3]
s = [3,3]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = gray, linewidth = 1, closed = True)
pgram.setmiterlimit(1)
pgram.draw()

restore()
endfigure()
