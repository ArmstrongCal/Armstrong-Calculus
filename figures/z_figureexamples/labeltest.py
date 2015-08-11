from figures import *

width=200
height=200
margin = 15
beginfigure("labeltest", 200, 200)
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5,1,5],[-5,1,5], color=lightgray)
grid.draw()

axes = Axes(labelalignment="lb", frame = "lb")
###
###  labelalignment is an option that shows how to display the labels
###     the first letter is either "l" or "r"
###         for left or right of the vertical axis
###     the second letter is either "b" or "t"
###         for bottom or top of the horizontal axis
###     This works no matter how the axes are positioned
###     The default is "lb"
###  frame is an option that shows where to draw the axes
###     the first letter is either "l", "c" or "r"
###         to put the vertical axis on the left, center or right
###     the second letter is "b", "c" or "t"
###         to put the horizontal axis on the bottom, center or top
###     Center means to draw the axes at x or y = 0
###     the default is "cc"

axes.draw()
axes.sethticks([-5,1,5])
axes.drawhticks()
axes.sethlabels([-5,1,5])
axes.drawhlabels()
axes.setvticks([-5,1,5])
axes.drawvticks()
axes.setvlabels([-5,1,5])
axes.drawvlabels()

point = [1,1]
p = Point(point, fillcolor=lightred)
p.fill()
p.draw()

### labels can also be aligned.  Specify a point in math coordinates
###    and an offset in points.  To understand the alignment, imagine
###    a box surrounding the label.  The box is placed so that the 
###    specified point is in a particular position relative to that point
###    the first letter is "l", "c", or "r" depending on whether the point
###        is on the left, center or right of the box
###    the second letter is "b", "c" or "t" depending on whether the point
###        is on the bottom, center or top of the box

label = Label(r"$y=x^2$", point, alignment = "rc", offset = [-3, 0], scale=2)
label.draw()

restore()
endfigure()
