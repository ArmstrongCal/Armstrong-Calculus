from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_6_LRMsum", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

axes.sethticks([1,7,8]) 
axes.drawhticks()

axes.sethlabels([1,7,8])
axes.drawhlabels()

label = Label(r"$y = f(x)$", [0.1,10], alignment = "lb", offset = [3,3])
label.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 5, #  g = Function(lambda x: x*x*x), 
                domain = [1,8], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()


#def f(x):
#    return -0.05*(x-4)**3+7

#point = Point([2, f(2)], 1.5)
#point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"LEFT", [4.5,-1], alignment = "cc", offset = [0,0])
label.draw()


restore()

#####################

save()
setupcoordinates([width + margin, margin, 2*width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

axes.sethticks([1,7,8]) 
axes.drawhticks()

axes.sethlabels([1,7,8])
axes.drawhlabels()

label = Label(r"$y = f(x)$", [0.1,10], alignment = "lb", offset = [3,3])
label.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 5, #  g = Function(lambda x: x*x*x), 
                domain = [1,8], fillcolor = boxcolor,
                style = RiemannSum.RIGHT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

#def f(x):
#    return -0.05*(x-4)**3+7

#point = Point([2, f(2)], 1.5)
#point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"RIGHT", [4.5,-1], alignment = "cc", offset = [0,0])
label.draw()

restore()


#####################

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-1, -2, 9, 12])

axes = Axes()
axes.draw()

axes.sethticks([1,7,8]) 
axes.drawhticks()

axes.sethlabels([1,7,8])
axes.drawhlabels()

label = Label(r"$y = f(x)$", [0.1,10], alignment = "lb", offset = [3,3])
label.draw()

f = Function(lambda x: -0.05*(x-4)**3+7)

rs = RiemannSum(f, 5, #  g = Function(lambda x: x*x*x), 
                domain = [1,8], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

#def f(x):
#    return -0.05*(x-4)**3+7

#point = Point([2, f(2)], 1.5)
#point.setfillcolor(pointcolor)
#point.fill()
#point.draw()

label = Label(r"MID", [4.5,-1], alignment = "cc", offset = [0,0])
label.draw()


restore()


endfigure()
