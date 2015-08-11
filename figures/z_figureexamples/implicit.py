from figures import *

width = 200
height = 200
margin = 2
beginfigure("implicit", width, height)

save()
xs = 3
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-xs, -xs, xs, xs])

Grid([-xs,0.5,xs], [-xs,0.5,xs], color=lightgray).draw()
Axes().draw()

def f(x,y):
    return y*y*y - x*x + 2*x*y

Implicit(f, 0, color=blue).draw()

def f(x,y):
    return y*y*y - x*x + 2*x*y - x

Implicit(f, 0, color=magenta, initialdepth=6).draw()

restore()
endfigure()
