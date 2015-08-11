from figures import *

width = 150
height = 150
margin = 5

## initialize the stuff you're going to use in each figure
def f(x):
    return -0.25*x*(x-6) + 1
a = 1

## put all the drawing code in a loop
h = [3, 1, 0.2]
for i in range(len(h)):
    beginfigure("secant." + str(i), width,height)
    save()
    setupcoordinates([margin, margin, width-margin, height-margin],
                     [-1,-1, 5, 5])
    
    Grid([-1,1,5], [-1,1,5], color = lightgray).draw()

    axes = Axes()
    axes.draw()

    ah = a+h[i]
    axes.sethticks([a, h[i], ah])
    axes.sethticksize(10)
    axes.drawhticks()

    Graph(Function(f), color=blue).draw()

    save()
    cliptoboundingbox()
    Line([a, f(a)], [ah, f(ah)], infinite=True, color=green).draw()
    restore()

    point = Point([a,f(a)], fillcolor=lightblue)
    point.fill()
    point.draw()

    point = Point([ah, f(ah)], fillcolor=lightgreen)
    point.fill()
    point.draw()
    
    if i != len(h)-1:
        Label(r"$a$", [a, 0], 
              offset=[0,-10], alignment = "ct").draw()
        Label(r"$a+h$", [ah, 0], offset=[0,-7], alignment = "ct").draw()
        Vector([ah-0.7, 0.3], tail=[ah, 0.3], fillcolor=gray, 
               arrowwidth=1.5).fill()

    restore()
    endfigure()
    
