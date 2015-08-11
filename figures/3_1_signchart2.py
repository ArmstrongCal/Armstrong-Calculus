from figures import *
from defaults import *

width = standardwidth*2.4
height = standardheight*0.8
beginfigure("3_1_signchart2", width, height)

margin = 30
save()
setupcoordinates([2*margin, 0.2*margin, width-0.2*margin, height-0.2*margin],
                 [-7, -2, 7, 4])

line = Line([-7,0],[7,0], color=black, linewidth = 1.5)
line.draw()

label = Label(r"sign($f'$)", [-7, 0.5], alignment = "rb", offset = [-2,0])
label.draw()

label = Label(r"behav($f$)", [-7, -0.5], alignment = "rt", offset = [-2,0])
label.draw()

#########

label = Label(r"$+--$", [-4.8, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [-4.8, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"INC", [-4.8, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = -math.sqrt(3)
line = Line([2*a,-0.25],[2*a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$-\sqrt{3}$", [2*a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$++-$", [-1.7, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [-1.7, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"DEC", [-1.7, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = 0
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$0$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$++-$", [1.7, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [1.7, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"DEC", [1.7, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

a = math.sqrt(3)
line = Line([2*a,-0.25],[2*a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\sqrt{3}$", [2*a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$+++$", [4.8, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [4.8, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"INC", [4.8, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


label = Label(r"$f'(x) = 3x^2(x+\sqrt{3})(x-\sqrt{3})$", [0, 3], alignment = "cb", offset = [0,2])
label.draw()



restore()

endfigure()
