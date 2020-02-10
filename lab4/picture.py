from graph import *
windowSize(800, 600)
canvasSize(800,600)

def cloud_paint(x,y):
    penColor(0, 0, 255)
    penSize(1)
    brushColor(190, 240, 255)
    circle(x, y, 25)
def treangle_paint(tree):
    penColor(0,0,0)
    penSize(1)
    brushColor(0,128,0)
    polygon(tree)


cloudlengs = 190
cloudhaigh = 65

num=1
numOfCircle=8

for i in range(0, numOfCircle, 1):
    cloudstep=25
    if num==4:
        cloudhaigh+=cloudstep
        cloudlengs=215
    cloud_paint(cloudlengs, cloudhaigh)
    cloudlengs-=cloudstep
    num+=1

treehaight = 3
maxX = 700
minY = 440

for i in range(0, treehaight, 1):
    treestep = 50
    bratchstep = 70
    a=maxX
    b=minY
    c=maxX-bratchstep
    d=minY-bratchstep
    e=c-bratchstep
    f=minY
    tree =[(a,b),(c,d),(e,f),(a,b)]
    treangle_paint(tree)
    minY-=treestep

penColor(0, 0, 0)
penSize(1)
brushColor(255, 255, 0)
circle(600, 90, 50)

run()