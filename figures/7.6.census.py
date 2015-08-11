data = [[1998,5932090951],
        [1999,6008254795],
        [2000,6083550220],
        [2001,6159242510],
        [2002,6234361771],
        [2005,6456443080],
        [2006,6530984631],
        [2007,6606214786],
        [2008,6681112529],
        [2009,6755987239],
        [2010,6830586985]]

percapita = []
x = 0
y = 0
xy = 0
x2 = 0
n = 0
for i in range(1, len(data)-1):
    if i == 5: 
        continue
    growth = (data[i+1][1] - data[i-1][1])/float((data[i+1][0]-data[i-1][0])*data[i][1])
    percapita.append([data[i][1], growth])
    x += data[i][1]
    y += growth
    n += 1
    xy += data[i][1]*growth
    x2 += data[i][1]*data[i][1]

    print data[i][1], growth

print x, y, n, xy, x2

m = (n*xy - x*y)/float(n*x2 - x*x)
b = (y - m*x)/float(n)
m *= 10**9

print m, b
carrying = -b/float(m)
print carrying


from figures import *
width=200
height=150

x0 = 6
x1 = 7
y0 = 0.010
y1 = 0.015
beginfigure("7_6_census", width, height)
setupcoordinates([33, 15, width-7, height-5],
                 [x0, y0, x1, y1])

Grid([x0,0.1,x1], [y0, 0.001, y1+0.0001], color=lightgray).draw()

axes=Axes(frame="lb")
axes.draw()
axes.setticks([x0,0.1,x1], [y0,0.001,y1+0.0001])
axes.drawticks()
axes.setlabels([x0,0.2,x1+0.001], [y0, 0.001, y1+0.001])
axes.drawlabels()

for p in percapita:
    x = p[0]/float(10**9)
    y = p[1]
    p = Point([x,y], 2.5, fillcolor=red)
    p.fill()
    p.draw()

Label(r"$P$", [7,0], offset=[-3,3],alignment="rb").draw()
Label(r"per capita growth rate", [x0,y1], offset=[3,-3],alignment="lt").draw()

endfigure()


x0 = 6
x1 = 7
y0 = 0.010
y1 = 0.015
beginfigure("7_6_census_1", width, height)
setupcoordinates([33, 15, width-7, height-5],
                 [x0, y0, x1, y1])

Grid([x0,0.1,x1], [y0, 0.001, y1+0.0001], color=lightgray).draw()

axes=Axes(frame="lb")
axes.draw()
axes.setticks([x0,0.1,x1], [y0,0.001,y1+0.0001])
axes.drawticks()
axes.setlabels([x0,0.2,x1+0.001], [y0, 0.001, y1+0.001])
axes.drawlabels()


Graph(Function(lambda x: m*x+b), color=blue).draw()

for p in percapita:
    x = p[0]/float(10**9)
    y = p[1]
    p = Point([x,y], 2.5, fillcolor=red)
    p.fill()
    p.draw()

Label(r"$P$", [7,0], offset=[-3,3],alignment="rb").draw()
Label(r"per capita growth rate", [x0,y1], offset=[3,-3],alignment="lt").draw()

endfigure()


x0 = 0
y0 = -0.01
x1 = 20
y1 = 0.03
beginfigure("7_6_census_2", width, height)
setupcoordinates([33, 15, width-7, height-5],
                 [x0, y0, x1, y1])

Grid([x0,2,x1], [y0, 0.01, y1+0.0001], color=lightgray).draw()

axes=Axes()
axes.draw()
axes.setticks([x0,2,x1], [y0,0.01,y1+0.0001])
axes.drawticks()
axes.setlabels([x0,2,x1], [y0, 0.01, y1+0.001])
axes.drawlabels()

gsave()
cliptoboundingbox()
Graph(Function(lambda x: m*x+b), color=blue).draw()
grestore()

for p in percapita:
    x = p[0]/float(10**9)
    y = p[1]
    p = Point([x,y], 2.5, fillcolor=red)
    p.fill()
    p.draw()

Label(r"$P$", [x0,0], offset=[-3,3],alignment="rb").draw()
Label(r"per capita growth rate", [x0,y1], offset=[3,-3],alignment="lt").draw()

endfigure()




