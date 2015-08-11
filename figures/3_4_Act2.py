from figures import *
from defaults import*

width = 180
height = 120
beginfigure("3_4_Act2", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,5,4])

p = [1,1]
q = [4,1]
r = [4,3]

points = [p,q,r]
triangle = Polygon(points = points, color = graphcolor, fillcolor = gray, linewidth = 1, closed = True)
triangle.draw()

line = Line([3.1,1], [4,3], linewidth = 1, dash = [4,4], color = gray)
line.draw()

line = Line([1,0.2], [4,0.2], linewidth = 1, color = gray)
line.draw()

label = Label("$3$", [2.5,0.3], alignment = "cb", offset = [0,2])
label.draw()

line = Line([4.8,1], [4.8,3], linewidth = 1, color = gray)
line.draw()

label = Label("$2$", [4.7,2], alignment = "rc", offset = [-2,0])
label.draw()


point = Point([1,1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4,1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4,3], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([3.1,1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()



label = Label("$P$", [1,1], alignment = "ct", offset = [0,-5])
label.draw()

label = Label("$Q$", [4,1], alignment = "ct", offset = [0,-5])
label.draw()

label = Label("$Z$", [3.1,1], alignment = "ct", offset = [0,-5])
label.draw()

label = Label("cabin", [4,3], alignment = "cb", offset = [0,5])
label.draw()


restore()
endfigure()
