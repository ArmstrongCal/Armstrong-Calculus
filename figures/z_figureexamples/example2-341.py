from figures import *

width = 200
height = 200
beginfigure("example2", width, height)

save()
setupcoordinates([0,0,width,height], [0,0,1,1])

p = [0.1, 0.1]
q = [0.8, 0.2]
r = [0.6, 0.9]

points = [p,q,r]
triangle = Polygon(points = points, fillcolor = lightblue,
                   color = blue, linewidth = 2, closed = True)
triangle.fill()

midp = pointonline(q, 0.5, r)
midq = pointonline(p, 0.5, r)
midr = pointonline(p, 0.5, q)

linep = Line(p, midp, color = lightred, linewidth = 1.3)
lineq = Line(q, midq, color = lightred, linewidth = 1.3)
liner = Line(r, midr, color = lightred, linewidth = 1.3)
linep.draw()
lineq.draw()
liner.draw()
triangle.draw()

median = pointonline(p, 2/float(3), midp)
point = Point(median, fillcolor = red)
point.fill()
point.draw()

labelp = Label("$P$", p, offset = [-10, 3])
labelp.draw()

labelq = Label("$Q$", q, offset = [2,2])
labelq.draw()

labelr = Label("$R$", r, offset = [4,0])
labelr.draw()



restore()
endfigure()
