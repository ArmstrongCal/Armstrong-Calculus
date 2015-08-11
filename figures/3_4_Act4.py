from figures import *
from defaults import*

width = 200
height = 100
beginfigure("3_4_Act4", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [0,0,6,3])


line = Line([0.5,1], [5.5,1], linewidth = 1, color = gray)
line.draw()

line = Line([1.75,1], [4.25,1], linewidth = 1, color = black)
line.draw()

label = Label("$2$", [3,0.5], alignment = "cb", offset = [0,2])
label.draw()

line = Line([1.75,1], [1.3,2.3], linewidth = 1, color = black)
line.draw()

line = Line([4.25,1], [4.7,2.3], linewidth = 1, color = black)
line.draw()

line = Line([1.3,2.3], [4.7,2.3], linewidth = 1, color = lightgray)
line.draw()

label = Label("$1$", [1.8,1.8], alignment = "rc", offset = [-2,0])
label.draw()

label = Label("$1$", [4.2,1.8], alignment = "lc", offset = [2,0])
label.draw()

label = Label(r"$\theta$", [1.75,1], alignment = "rb", offset = [-8,4])
label.draw()

restore()
endfigure()
