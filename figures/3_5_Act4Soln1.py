from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("3_5_Act4Soln1", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,2,2])

label = Label("$90$", [1.5,0.5], alignment = "lt", offset = [2,-2])
label.draw()

label = Label("$x$", [0.8,0.2], alignment = "rt", offset = [-2,-2])
label.draw()

label = Label("$z$", [1.2,0.8], alignment = "rt", offset = [-2,-2])
label.draw()

line = Line([0,1], [1,0], linewidth = graphwidth, color = gray)
line.draw()

line = Line([0,1], [1,2], linewidth = graphwidth, color = gray)
line.draw()

line = Line([2,1], [1,0], linewidth = graphwidth, color = graphcolor)
line.draw()

line = Line([2,1], [1,2], linewidth = graphwidth, color = gray)
line.draw()

line = Line([0.6,0.4], [2,1], linewidth = graphwidth, color = graphcolor, dash = [4,4])
line.draw()

line = Line([0.6,0.4], [1,0], linewidth = graphwidth, color = graphcolor)
line.draw()

point = Point([0.6,0.4], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


restore()
endfigure()
