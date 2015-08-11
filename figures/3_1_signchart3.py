from figures import *
from defaults import *

width = standardwidth*2.4
height = standardheight*0.8
beginfigure("3_1_signchart3", width, height)

margin = 30
save()
setupcoordinates([2*margin, 0.2*margin, width-0.2*margin, height-0.2*margin],
                 [-7, -2, 7, 4])

line = Line([-7,0],[7,0], color=black, linewidth = 1.5)
line.draw()

label = Label(r"sign($f''$)", [-7, 0.5], alignment = "rb", offset = [-2,0])
label.draw()

label = Label(r"behav($f$)", [-7, -0.5], alignment = "rt", offset = [-2,0])
label.draw()

#########

label = Label(r"$---$", [-4.8, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [-4.8, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"CCD", [-4.8, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = -math.sqrt(1.5)
line = Line([2*a,-0.25],[2*a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$-\sqrt{\frac{3}{2}}$", [2*a-0.2, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$-+-$", [-1.2, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [-1.2, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"CCU", [-1.2, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


a = 0
line = Line([a,-0.25],[a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$0$", [a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$++-$", [1.2, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$-$", [1.2, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"CCD", [1.2, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

a = math.sqrt(1.5)
line = Line([2*a,-0.25],[2*a,0.25], color=black, linewidth = 1.5)
line.draw()

label = Label(r"$\sqrt{\frac{3}{2}}$", [2*a, -0.5], alignment = "ct", offset = [0,-2])
label.draw()

##

label = Label(r"$+++$", [4.8, 1.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"$+$", [4.8, 0.6], alignment = "cb", offset = [0,0])
label.draw()

label = Label(r"CCU", [4.8, -0.5], alignment = "ct", offset = [0,-2])
label.draw()


label = Label(r"$f''(x) = 12x\left(x+\sqrt{\frac{3}{2}}\right)\left(x-\sqrt{\frac{3}{2}}\right)$", [0, 3], alignment = "cb", offset = [0,2])
label.draw()



restore()

endfigure()
