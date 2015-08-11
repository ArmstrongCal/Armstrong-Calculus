from figures import *
from defaults import*

width = 140
height = 120
beginfigure("3_5_Act1Soln", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
		 [-7,-9,7,3])

line = Line([0,-8], [6,0], linewidth = graphwidth, color = black)
line.draw()

line = Line([0,-8], [-6,0], linewidth = graphwidth, color = black)
line.draw()

def f(x):
    return -math.sqrt(1 - x**2/36)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(black)
graph.setlinewidth(graphwidth)
graph.setdomain([-5.999,5.999])
graph.draw()

def f(x):
    return math.sqrt(1 - x**2/36)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(black)
graph.setlinewidth(graphwidth)
graph.setdomain([-5.999,5.999])
graph.draw()

line = Line([0,-8], [0,0], linewidth = 1, color = gray)
line.draw()

line = Line([6,0], [0,0], linewidth = 1, color = gray)
line.draw()

def f(x):
    return -3.8-math.sqrt(1 - x**2/9)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.999,2.999])
graph.draw()

def f(x):
    return -3.8+math.sqrt(1 - x**2/9)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.999,2.999])
graph.draw()

line = Line([0,-8], [0,0], linewidth = 1, color = gray)
line.draw()

line = Line([6,0], [0,0], linewidth = 1, color = gray)
line.draw()

line = Line([0,-8], [0,-4], linewidth = 1, color = graphcolor)
line.draw()

line = Line([3,-4], [0,-4], linewidth = 1, color = graphcolor)
line.draw()

label = Label("$r$", [1.5,-3.9], alignment = "cb", offset = [0, 2])
label.draw()

label = Label("$h$", [0,-6], alignment = "lc", offset = [2, 0])
label.draw()

line = Line([-7,-8], [-7,0], linewidth = 1, color = gray)
line.draw()

line = Line([6,1.5], [0,1.5], linewidth = 1, color = gray)
line.draw()

label = Label("$6$", [3,1.5], alignment = "cb", offset = [0, 4])
label.draw()

label = Label("$8$", [-7,-4], alignment = "lc", offset = [4, 0])
label.draw()

restore()
endfigure()
