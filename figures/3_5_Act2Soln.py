from figures import *
from defaults import*

width = 180
height = 120
beginfigure("3_5_Act2Soln", width, height)

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

label = Label("$4000$", [2.5,0.5], alignment = "cb", offset = [0,2])
label.draw()

label = Label("$h$", [4.1,2], alignment = "lc", offset = [2,0])
label.draw()

label = Label("$z$", [2.5,2.05], alignment = "rb", offset = [-2,2])
label.draw()

label = Label(r"$\theta$", [1.5,1.05], alignment = "lb", offset = [6,2])
label.draw()

point = Point([1,1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4,3], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label("camera", [1,1], alignment = "rc", offset = [-6,0])
label.draw()

label = Label("rocket", [4,3], alignment = "cb", offset = [0,5])
label.draw()


restore()
endfigure()
