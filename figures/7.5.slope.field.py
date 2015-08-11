from figures import *

width=150
height=150
margin = 5

beginfigure("7.5.slope.field", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0, 0, 3, 3])

axes = Axes()
axes.draw()
#axes.sethticks([0, 1.5, 1.5])
#axes.drawhticks()

def f(t, P):
    return 1.5-P
SlopeField(f, [0,0.5,3], [0,0.5,3], color=green).draw()


Label(r"$t$", [3,0], offset=[0,3], alignment="rb").draw()
Label(r"$P$", [0,3], offset=[3,-3], alignment="lt").draw()
#Label(r"$1.5\cdot10^5$", [1.5, 0], offset=[3,3], alignment="lb"). draw()

endfigure()
