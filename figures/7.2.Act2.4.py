from figures import *

margin = 5
width = 120
height = 120

beginfigure("7.2.Act2.4", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 3, 3])

axes = Axes()
axes.draw()

dx = 0.75
ybar = 1

Graph(Function(lambda x: -(x-ybar)-0.5*(x-ybar)**2), domain=[ybar-dx, ybar+dx], color=blue).draw()

newpath()
axes.sethticks([1,1,1])
axes.drawhticks()

Label(r"$\overline{y}$", [ybar,0], offset=[0,-8], alignment="ct").draw()
Label(r"$y$", [3,0], offset=[-3,3], alignment="rb").draw()
Label(r"$\frac{dy}{dt}=f(y)$", [0,3], offset=[3,-3], alignment="lt").draw()


endfigure()
