from figures import *

width = 120
height = 120
margin = 5
lbmargin = 5

x0 = 0
x1 = 1
y0 = 0
y1 = 1

beginfigure("7.3.euler", width, height)
setupcoordinates([lbmargin, lbmargin, width-margin, height-margin],
                 [x0, y0, x1, y1])

Box([x0, y0, x1, y1],color=lightgray).draw()

axes = Axes()
axes.draw()

def f(x):
    return 0.8*x + 1
Graph(Function(f), color=blue).draw()

p0 = [2, f(2)]
p1 = [5, f(5)]

newpath()
moveto(p0)
lineto(p1[0], p0[1])
lineto(p1)
stroke(gray)

p = Point(p0, fillcolor=red)
p.fill()
p.draw()
p = Point(p1, fillcolor=red)
p.fill()
p.draw()

Label(r"$t$", [x1,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,y1], offset=[3,-3], alignment="lt").draw()

Label(r"$\Delta t$", [ (p0[0]+p1[0])/2., p0[1]], offset=[0,-3], alignment="ct").draw()
Label(r"$\Delta y$", [ p1[0], (p0[1]+p1[1])/2.], offset=[3,0], alignment="lc").draw()

endfigure()
