from graph import *

def update():
    moveObjectBy(obj, 5,0)
    if xCoord(obj) >=380:
        close()



class GraphObject(object):
    def __init__(self, obj, id='', dx=100, dy=100, delta=5):
        self.id = id
        self.obj = obj
        self.dx = dx
        self.dy = dy
        self.delta = delta
    def onLeft(self):
        cy = yCoord(self.obj)
        moveObjectBy(self.obj, -1 * self.delta, 0)
        if xCoord(self.obj) <= 0:
            moveObjectTo(self.obj, self.dx, cy)
    def onRight(self):
        cy = yCoord(self.obj)
        moveObjectBy(self.obj, self.delta, 0)
        if xCoord(self.obj) >= self.dx:
            moveObjectTo(self.obj, 0, cy)
    def onUp(self):
        cx = xCoord(self.obj)
        moveObjectBy(self.obj, 0, -1 * self.delta)
        if yCoord(self.obj) <= 0:
            moveObjectTo(self.obj, 0, self.dy)
    def onDown(self):
        cx = xCoord(self.obj)
        moveObjectBy(self.obj, 0, self.delta)
        if yCoord(self.obj) > self.dy:
            moveObjectTo(self.obj, cx, 0)

brushColor("blue")
rectangle(0,0,600,600)
brushColor("green")
rectangle(0,0,400,400)

evtList = []
penColor("pink")
brushColor("pink")
evtList.append(GraphObject(rectangle(0, 0, 50, 50), 'XX1', 600, 600, 10))

penColor("yellow")
brushColor("yellow")
evtList.append(GraphObject(rectangle(100, 100, 120, 120), 'XX2', 400, 400, 5))

penColor("grey")
brushColor("grey")
evtList.append(GraphObject(rectangle(200, 200, 240, 220), 'XX2', 500, 500, 15))


def keyPressed(e):
    global evtList
    if e.keycode == VK_ESCAPE:
        close()
    if e.keycode == VK_LEFT:
        for o in evtList:
            o.onLeft()
    if e.keycode == VK_RIGHT:
        for o in evtList:
            o.onRight()
    if e.keycode == VK_UP:
        for o in evtList:
            o.onUp()
    if e.keycode == VK_DOWN:
        for o in evtList:
            o.onDown()

onKey(keyPressed)


#ls = [obj, obj2]
#onKey(keyPressed(obj2))
#onTimer(update, 1000)


run()