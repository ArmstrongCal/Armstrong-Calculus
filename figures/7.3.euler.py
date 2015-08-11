from figures import *

width = 120
height = 120
margin = 8
lbmargin = 15

x0 = 0
x1 = 1.2
y0 = 0
y1 = 1.2

N = 2
beginfigure("7.3.euler.points."+str(N), width, height)
setupcoordinates([lbmargin+5, lbmargin, width-margin, height-margin],
                 [x0, y0, x1, y1])

xrange = [x0,0.2,x1]
yrange = [y0,0.2,y1]
Grid(xrange, yrange, color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks(xrange,yrange)
axes.setlabels([x0, 0.4, x1+0.1],[y0,0.4,y1+0.1])
axes.drawticks()
axes.drawlabels()

from math import *
#Graph(Function(lambda x: x + 2*exp(-x) - 1), color=blue).draw()

def f(t,y):
    return t-y

euler = [[0,1]]
dt = 0.2
for i in range(N):
    p = euler[-1]
    t = p[0]
    y = p[1]
    m = f(t,y)
    t += dt
    y += m*dt
    euler.append([t,y])

newpath()
moveto(euler[0])
for p in euler:
    lineto(p)
stroke(darkmagenta)

count = 0
for p in euler:
    point = Point(p, 2.5, fillcolor=red)
    point.fill()
    point.draw()
    cs = str(count)
    s = r"$(t_"+cs+",y_"+cs+")$"
    Label(s, p, scale=0.9,offset=[5,0],alignment="lc").draw()
    count += 1


Label(r"$t$", [x1,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,y1], offset=[3,-3], alignment="lt").draw()

endfigure()
