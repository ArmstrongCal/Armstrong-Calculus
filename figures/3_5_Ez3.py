from figures import *
from defaults import*

width = 200
height = 100
beginfigure("3_5_Ez3", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [-0.5,-0.5,5.5,3.5])


p = [0,0]
q = [0,1]
r = [4,1]
s = [4,0.8]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = gray, linewidth = 1.5, closed = True)
pgram.setmiterlimit(1)
pgram.draw()

p = [1,2]
q = [0,1]
r = [4,1]
s = [5,2]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = gray, linewidth = 1.5, closed = True)
pgram.setmiterlimit(1)
pgram.draw()

p = [5,2]
q = [4,1]
r = [4,0.8]
s = [5,1.8]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = gray, linewidth = 1.5, closed = True)
pgram.setmiterlimit(1)
pgram.draw()

line = Line([0,0], [3,1], linewidth = 1, dash = [4,4], color = gray)
#line.draw()

label = Label("$15$", [0,0.5], alignment = "rc", offset = [-4,0])
label.draw()

label = Label("$60$", [2,1], alignment = "cb", offset = [0,4])
label.draw()

label = Label("$25$", [0.5,1.5], alignment = "rb", offset = [-4,2])
label.draw()

label = Label("$3$", [5,1.9], alignment = "lc", offset = [4,0])
label.draw()


restore()
endfigure()
