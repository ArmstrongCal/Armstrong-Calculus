from figures import *

beginfigure('example12', 150, 150)
setupcoordinates([0,0,150,150],[-3,-3,3,3])

def f(x):
    return x**3 - x

function = Function(f)
derivative = function.differentiate()
secondderivative = derivative.differentiate()

Graph(function, color=blue, dash = [4,4]).draw()
Graph(derivative, color=red, dash = [8, 2]).draw()
Graph(secondderivative, color=green, dash=[1, 4]).draw()

endfigure()
