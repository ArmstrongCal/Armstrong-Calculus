from figures import *
from defaults import *

width = standardwidth*1.2
height = standardheight*0.8
beginfigure("3_2_signchartg", width, height)

margin = 30
save()
setupcoordinates([2*margin, 0.2*margin, width-0.2*margin, height-0.2*margin],
                 [-3, -2, 3, 4])

line = Line([-3,0],[3,0], color=black, linewidth = 1.5)
line.draw()

label = Label(r"sign($g'$)", [-3, 0.5], alignment = "rb", offset = [-2,0])
label.draw()

label = Label(r"behav($g$)", [-3, -0.5], alignment = "rt", offset = [-2,0])
label.draw()

#########

label = Label(r"$++$", [-1.5, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [-1.5, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"INC", [-1.5, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = 0
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\frac{1}{b}$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

label = Label(r"$+-$", [1.5, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [1.5, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"DEC", [1.5, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


label = Label(r"$g'(x) = ae^{-bx}(1-bx)$", [0, 3], alignment = "cb", offset = [0,2])
label.draw()

restore()

endfigure()
