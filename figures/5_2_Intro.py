from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_2_Intro", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -4.5, 4.5, 23])

xrange = [-1, 5.5, 4.5]
yrange = [-4.5, 27.5, 23]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1,1,4]) 
axes.setvticks([5,5,20])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([10,10,20])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([1,1,4])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()


label = Label(r"$f(x)=x^2$", [3,9], alignment = "rb", offset = [-2, 2] )
label.draw()


### first original function graph

def f(x):
    return x**2

area = AreaBetweenCurves(Function(f), fillcolor = lightblue, domain=[1,4])
area.fill()
area.draw()


cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.draw()

point = Point([1, f(1)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([4, f(4)], 1.5)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


label = Label(r"$\int_1^4 x^2 \, dx = 21$", [2.8, 2], alignment = "cc", offset = [0, 0])
label.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin, margin, 2*width-margin, height-margin], 
                 [-1, -4.5, 4.5, 23])

xrange = [-1, 5.5, 4.5]
yrange = [-4.5, 27.5, 23]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1,1,4]) 
axes.setvticks([5,5,20])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([10,10,20])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([1,1,4])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()

label = Label(r"$F(x)=\frac{1}{3}x^3$", [3,9], alignment = "rb", offset = [-2, 2] )
label.draw()



def f(x):
    return 0.3333*x**3

cliptoboundingbox()
graph = Graph(Function(f), color = graphcolor, linewidth = 1.5)
graph.draw()

line = Line([1,0],[1,f(1)], color = darkgray)
line.draw()

point = Point([1, f(1)], 1.5)
point.setfillcolor(cyan)
point.fill()
point.draw()

line = Line([4,0],[4,f(4)], color = darkgray)
line.draw()

point = Point([4, f(4)], 1.5)
point.setfillcolor(cyan)
point.fill()
point.draw()


label = Label(r"$(1,\frac{1}{3})$", [1, 0.333], alignment = "rb", offset = [-2, 2])
label.draw()

label = Label(r"$(4,\frac{64}{3})$", [4, 21.333], alignment = "rt", offset = [-3, -1])
label.draw()

label = Label(r"$F(4) - F(1) = 21$", [2, 15], alignment = "cc", offset = [0, 0])
label.draw()

restore()

endfigure()
