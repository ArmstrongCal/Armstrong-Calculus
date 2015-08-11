from figures import *
from defaults import*

width = standardwidth
height = standardheight
beginfigure("2_6_cosarctan", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,1,1])

p = [0.3, 0.1]
q = [0.6, 0.1]
r = [0.6, 0.8]

points = [p,q,r]
triangle = Polygon(points = points, color = graphcolor, linewidth = 2, closed = True)
#triangle.fill()
triangle.draw()

label = Label(r"$x$", [0.65, 0.4], alignment = "lb", offset = [-2, 0])
label.draw()

label = Label(r"$\sqrt{1+x^2}$", [0.375, 0.4], alignment = "rb", offset = [2, 0])
label.draw()

label = Label(r"$\theta$", [0.375, 0.17], alignment = "lc", offset = [-2, 0])
label.draw()

label = Label("$1$", [0.45, 0.025], alignment = "cc", offset = [0, 0])
label.draw()


restore()
endfigure()
