from figures import *

xs = 0.25
ys = 0.25
dx = 0.05
width=120
height=120
lbmargin = 20
rtmargin = 5

beginfigure("7.3.error", width, height)
setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
                 [0,0,xs, ys])

Grid([0, dx, xs], [0, dx, ys], color=lightgray).draw()
axes = Axes()
axes.draw()
axes.setticks([0,0.1,xs], [0,0.1,ys])
axes.setlabels([0,0.1,xs], [0,0.1,ys])
axes.drawticks()
axes.drawlabels()

points = [[0.2000,0.2300],
          [0.1000,0.1245],
          [0.0500,0.0650],
          [0.0250,0.0332]]

for p in points:
    p = Point(p, size=2.5, fillcolor = red)
    p.fill()
    p.draw()

Label("Error", [0,ys], offset=[3,-3], alignment="lt").draw()
Label(r"$\Delta t$", [xs,0], offset=[-3,3], alignment="rb").draw()


endfigure()
