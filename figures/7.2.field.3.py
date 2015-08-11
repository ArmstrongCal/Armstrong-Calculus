from figures import *

width = 120
height = 120
margin = 5

def f(t,y):
    return t - 2

for r in range(4):
    beginfigure("7.2.field.3"+str(r), width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],
                     [-0.5, -2, 3.5, 3])

    Grid([-0.5,0.5,3.5], [-2,0.5,3], color=lightgray).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-0.5,0.5,3.5], [-2,0.5,3])
    axes.drawticks()
    axes.setlabels([0,1,3], [-2,1,3])
    axes.drawlabels()


    Label(r"$t$", [3.5,0], offset=[-3,3], alignment="rb").draw()
    Label(r"$y$", [0,3], offset=[3,-3], alignment="lt").draw()

    SlopeField(f,[0, 0.5, 3], [-2, 0.5, 3], color=lightgreen).draw()

    Graph(Function(lambda x: 0.5*x*x-2*x+1), color=blue, domain=[0,r+0.5]).draw()

    endfigure()
