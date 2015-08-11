from figures import *

width=150
height=150
margin = 5

beginfigure("7.5.lake.michigan", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0, -1.5, 3, 1.5])

axes = Axes()
axes.draw()
axes.sethticks([0, 1.5, 1.5])
axes.drawhticks()

Graph(Function(lambda x: 0.8*(1.5 - x)), color=blue).draw()

Label(r"$P$", [3,0], offset=[0,3], alignment="rb").draw()
Label(r"$dP/dt$", [0,1.5], offset=[3,-3], alignment="lt").draw()
Label(r"$1.5\cdot10^5$", [1.5, 0], offset=[3,3], alignment="lb"). draw()

endfigure()
