from figures import *
from defaults import *

width = 120
height = 160

beginfigure("4_2_PA1", 3*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-0.5,-0.5,2.5,3.5])

grid = Grid([-0.5,0.25,2.5], 
            [-0.5,0.25,3.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,2], # you can do this separately with seth(v)labels
               [1,1,3])
axes.drawlabels()

f = Function(lambda x : .25*x**3-1.50*x**2+3.00*x+.25)

rs = RiemannSum(f, 4, #  g = Function(lambda x: x*x*x), 
                domain = [0,2], fillcolor = boxcolor,
                style = RiemannSum.LEFT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.25,2.25])
graph.draw()

rs.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2,2.5], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$A_1$", [0.25,-0.25], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_2$", [0.75,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_3$", [1.25,0.75], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_4$", [1.75,1.0], alignment = "cc", offset = [0, 0] )
label.draw()

def f(x):
    return .25*x**3-1.50*x**2+3.00*x+.25

p1 = Point([0,f(0)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([0.5,f(0.5)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1,f(1)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1.5,f(1.5)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

###

save()
margin = 10
setupcoordinates([width + margin,margin,2*width-margin,height-margin], 
                 [-0.5,-0.5,2.5,3.5])

grid = Grid([-0.5,0.25,2.5], 
            [-0.5,0.25,3.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,2], # you can do this separately with seth(v)labels
               [1,1,3])
axes.drawlabels()

f = Function(lambda x : .25*x**3-1.50*x**2+3.00*x+.25)

rs = RiemannSum(f, 4, #  g = Function(lambda x: x*x*x), 
                domain = [0,2], fillcolor = boxcolor,
                style = RiemannSum.RIGHT) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.25,2.25])
graph.draw()

rs.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2,2.5], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$B_1$", [0.25,0.25], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$B_2$", [0.75,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$B_3$", [1.25,0.75], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$B_4$", [1.75,1], alignment = "cc", offset = [0, 0] )
label.draw()

def f(x):
    return .25*x**3-1.50*x**2+3.00*x+.25

p1 = Point([0.5,f(0.5)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1,f(1)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1.5,f(1.5)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([2,f(2)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()


restore()

####

save()
margin = 10
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin], 
                 [-0.5,-0.5,2.5,3.5])

grid = Grid([-0.5,0.25,2.5], 
            [-0.5,0.25,3.5], 
            color = lightlightgray)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,1,3])
axes.drawticks()

axes.setlabels([1,1,2], # you can do this separately with seth(v)labels
               [1,1,3])
axes.drawlabels()

f = Function(lambda x : .25*x**3-1.50*x**2+3.00*x+.25)

rs = RiemannSum(f, 4, #  g = Function(lambda x: x*x*x), 
                domain = [0,2], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.setdomain([-0.25,2.25])
graph.draw()

rs.draw()

label = Label("mph", [0.1,3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2,0.1], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y= v(t)$", [2,2.5], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$C_1$", [0.25,0.25], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$C_2$", [0.75,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$C_3$", [1.25,0.75], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$C_4$", [1.75,1.0], alignment = "cc", offset = [0, 0] )
label.draw()

def f(x):
    return 0.25*x**3-1.50*x**2+3.00*x+.25

p1 = Point([0.25,f(0.25)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([0.75,f(0.75)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1.25,f(1.25)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([1.75,f(1.75)], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()


endfigure()
