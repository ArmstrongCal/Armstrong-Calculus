from figures import *
from defaults import*

width = 200
height = 100
beginfigure("3_5_ConeEx", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [-4,-1,4,3])

line = Line([0,2], [4,0], linewidth = graphwidth, color = graphcolor)
line.draw()

line = Line([0,2], [-4,0], linewidth = graphwidth, color = graphcolor)
line.draw()

line = Line([0,2], [0,0], linewidth = 1, color = gray)
line.draw()

line = Line([4,0], [0,0], linewidth = 1, color = gray)
line.draw()

def f(x):
    return -math.sqrt(0.25 - x**2/64)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3.999,3.999])
graph.draw()

def f(x):
    return math.sqrt(0.25 - x**2/64)-0.05

function = Function(f)
Graph(function, color=graphcolor, linewidth = graphwidth, domain=[-3.99,3.99], dash = [4,4]).draw()

label = Label("$r$", [2,0], alignment = "cb", offset = [0, 2])
label.draw()

label = Label("$h$", [0,1], alignment = "lc", offset = [2, 0])
label.draw()


restore()
endfigure()
