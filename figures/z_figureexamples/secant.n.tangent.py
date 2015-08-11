from figures import *

width = 150
height = 150
margin = 5

def f(x):
    return -0.25*x*(x-6) + 1
a = 1

h = [3, 1, 0.2]
beginfigure("secant.n.tangent", width,height)
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1, 5, 5])
    
Grid([-1,1,5], [-1,1,5], color = lightgray).draw()

axes = Axes()
axes.draw()

axes.sethticks([a, 1, a])
axes.sethticksize(10)
axes.drawhticks()

Graph(Function(f), color=blue).draw()

save()
cliptoboundingbox()
for i in range(len(h)):
    ah = a+h[i]
    Line([a, f(a)], [ah, f(ah)], infinite=True, color=green).draw()

tangent = Function(f).tangentline(a)
Graph(tangent, color=red, linewidth=1.3).draw()
restore()

point = Point([a,f(a)], fillcolor=lightblue)
point.fill()
point.draw()

Label(r"$a$", [a, 0], 
      offset=[0,-10], alignment = "ct").draw()

restore()
endfigure()
    
