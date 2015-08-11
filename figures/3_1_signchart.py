from figures import *
from defaults import *

width = standardwidth*1.6
height = standardheight*0.8
beginfigure("3_1_signchart", width, height)

margin = 30
save()
setupcoordinates([2*margin, 0.2*margin, width-0.2*margin, height-0.2*margin],
                 [-3, -2, 5, 4])

line = Line([-3,0],[5,0], color=black, linewidth = 1.5)
line.draw()

label = Label(r"sign($f'$)", [-3, 0.5], alignment = "rb", offset = [-2,0])
label.draw()

label = Label(r"behav($f$)", [-3, -0.5], alignment = "rt", offset = [-2,0])
label.draw()

#########

label = Label(r"$+++$", [-2, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [-2, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"INC", [-2, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = -1
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$-1$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

label = Label(r"$+++$", [1, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [1, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"INC", [1, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

a = 3
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$3$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

label = Label(r"$+-+$", [4, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [4, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"DEC", [4, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


label = Label(r"$f'(x) = e^{-2x}(3-x)(x+1)^2$", [1, 3], alignment = "cb", offset = [0,2])
label.draw()



restore()

endfigure()
