from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("3_5_Act3Soln", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [-1,-1,16,16])

label = Label("$15$", [0,8], alignment = "rc", offset = [-2,0])
label.draw()

label = Label("$x$", [4,0], alignment = "ct", offset = [0,-4])
label.draw()

label = Label("$s$", [10.7,0], alignment = "ct", offset = [0,-4])
label.draw()

label = Label(r"$6$", [8,3], alignment = "rc", offset = [-2,0])
label.draw()

line = Line([0,0], [0,15], linewidth = graphwidth, color = black)
line.draw()

line = Line([0,0], [13.333,0], linewidth = graphwidth, color = black)
line.draw()

line = Line([8,0], [8,6], linewidth = graphwidth, color = graphcolor)
line.draw()

line = Line([0,15], [13.333,0], linewidth = graphwidth, color = gray, dash = [4,4])
line.draw()

point = Point([0,15], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([8,0], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([13.333,0], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label("lamp", [0,15], alignment = "cb", offset = [0,2])
label.draw()


restore()
endfigure()
