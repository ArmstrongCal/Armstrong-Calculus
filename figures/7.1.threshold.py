from figures import *

margin = 5
width = 150
height = 150

beginfigure("7.1.threshold", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0,-4, 4, 4])

xrange = [0, 1, 4]
yrange = [-4,1,4]
Grid(xrange, yrange, color=lightgray).draw()

axes = Axes()
axes.draw()
axes.sethticks(xrange)
axes.drawhticks()
axes.sethlabels(xrange)
axes.drawhlabels()

Label(r"$P$", [4,0], offset=[-3,3], alignment="rb").draw()
Label(r"$\displaystyle\frac{dP}{dt}$", [0,4], offset=[3,-3], alignment="lt").draw()

cliptoboundingbox()
f = Function(lambda x: -(x-3)*(x-1)*x)
Graph(f, color=blue).draw()

endfigure()
