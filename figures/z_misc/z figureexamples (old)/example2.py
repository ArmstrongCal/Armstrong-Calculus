from figures import *

width = 200
height = 200
beginfigure("example2", width, height)

save()
setupcoordinates([0,0,width,height], [0,0,1,1])

p = [0.1, 0.1]
q = [0.8, 0.2]
r = [0.6, 0.9]

triangle = Polygon()
triangle.addpoint(p)
triangle.addpoint(q)
triangle.addpoint(r)    # or triangle.addpoints([p, q, r])
triangle.close()        # always do this for a closed polygon
                        #   you can use a polygon for a sequence of line segs
triangle.setfillcolor(lightblue)
triangle.setcolor(blue)
triangle.setlinewidth(2)
triangle.fill()

midp = pointonline(q, 0.5, r)
midq = pointonline(p, 0.5, r)
midr = pointonline(p, 0.5, q)

linep = Line(p, midp)
lineq = Line(q, midq)
liner = Line(r, midr)
linep.setcolor(lightred)
lineq.setcolor(lightred)
liner.setcolor(lightred)
linep.setlinewidth(1.3)
lineq.setlinewidth(1.3)
liner.setlinewidth(1.3)
linep.draw()
lineq.draw()
liner.draw()
triangle.draw()

median = pointonline(p, 2/float(3), midp)
point = Point(median, 3)
point.setfillcolor(red)
point.fill()
point.draw()

labelp = Label("$P$", p)
labelp.setoffset([-10,3])
labelp.draw()

labelq = Label("$Q$", q)
labelq.setoffset([2,2])
labelq.draw()

labelr = Label("$R$", r)
labelr.setoffset([4,0])
labelr.draw()



restore()
endfigure()
