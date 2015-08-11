from figures import *
width=200
height=150

x0 = 0
x1 = 20
y0 = -0.1
y1 = 0.1
beginfigure("7_6_logistic_de", width, height)
setupcoordinates([33, 5, width-7, height-5],
                 [x0, y0, x1, y1])

#Grid([x0,0.1,x1], [y0, 0.001, y1], color=lightgray).draw()

axes=Axes()
axes.draw()
axes.setticks([x0,2,x1], [y0,0.05,y1])
axes.drawticks()
axes.setlabels([x0,2,x1], [y0, 0.05, y1])
axes.drawlabels()

gsave()
cliptoboundingbox()
Graph(Function(lambda P: P*(0.025 - 0.002*P)), color=blue).draw()
grestore()

Label(r"$P$", [x1,0], offset=[-3,3],alignment="rb").draw()
Label(r"$\frac{dP}{dt}$", [0,y1], offset=[3,-3],alignment="lt").draw()

endfigure()




