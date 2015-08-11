from figures import *

width = 200
height = 200
margin = 2
beginfigure("example10", width, height)

save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2, 2, 2])

def f(x,y):
    return x*x + y*y

Grid([-2,0.5,2], [-2,0.5,2], color=lightgray).draw()
Axes().draw()

Implicit(f, 2, color=blue).draw()

def leminiscate(x,y):
    return x**4 - x*x + y*y
Implicit(leminiscate, 0, color=orange).draw()

def folium(x,y):
    x*=4.5
    y*=4.5
    return x**3 + y**3 - 9*x*y
Implicit(folium, 0, color=magenta).draw()

restore()
endfigure()
