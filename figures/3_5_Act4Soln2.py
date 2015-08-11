from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("3_5_Act4Soln2", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,2,2])

label = Label("$r$", [1.05,0.05], alignment = "lt", offset = [2,-2])
label.draw()

label = Label("$x$", [0.8,0.2], alignment = "rt", offset = [-2,-2])
label.draw()

label = Label("$s$", [0.87,0.24], alignment = "lb", offset = [2,2])
label.draw()

line = Line([0,1], [1,0], linewidth = graphwidth, color = gray)
line.draw()

line = Line([0,1], [1,2], linewidth = graphwidth, color = gray)
line.draw()

line = Line([2,1], [1,0], linewidth = graphwidth, color = gray)
line.draw()

line = Line([2,1], [1,2], linewidth = graphwidth, color = gray)
line.draw()

line = Line([0.6,0.4], [1.1,0.1], linewidth = graphwidth, color = graphcolor, dash = [4,4])
line.draw()

line = Line([0.6,0.4], [1,0], linewidth = graphwidth, color = graphcolor)
line.draw()

line = Line([1.1,0.1], [1,0], linewidth = graphwidth, color = graphcolor)
line.draw()

point = Point([0.6,0.4], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([1.1,0.1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()



restore()
endfigure()
