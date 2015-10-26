
#
# Plot points in simple graph
#

from graphics import GraphicsWindow
from math import sin
from math import cos

#
# creates a grid on a canvas for drawing points
#
def createGrid(canvas,maxx,maxy):
    # Draw the coordinate system; but invert graph so that plot starts in lower left.
    # - assumes a 500-by-500 canvas
    #
    #  Parameters:
    #   - canvas - the canvas being used for plotting
    #   - maxx is the maximum value of a point in the x-direction
    #   - maxy is the maximum value of a point in the y-direction
    half = 5
    canvas.drawLine(50, 50, 450, 50)
    canvas.drawLine(50, 50, 50, 450)
    canvas.drawLine(450,50,450,450)
    canvas.drawLine(50,450,450,450)
    # assumes 40 tick marks on grid in y direction .. 50 to 450 of canvas
    stepy = round(maxy/40)
    for y in range(0,maxy,stepy) :
        yy = round(y/maxy*400)
        canvas.drawLine(50-half,50+yy,50+half,50+yy)
    canvas.drawText(2,40,str(maxy))
    canvas.drawText(2,440,"  0")
    # assumes 40 tick marks on grid in y direction .. 50 to 450 of canvas
    stepx = round(maxx/40)
    for x in range(0,maxx,stepx):
        xx = round(x/maxx*400)
        canvas.drawLine(xx+50,450-half,xx+50,450+half)
    canvas.drawText(40,460," 0")
    canvas.drawText(420,460,str(maxx))

def drawDots(canvas,x,maxx,y,maxy,color):
    # Draw dots of a given color on a grid created by createGrid
    # Assumes that all x, y values are in range 0-maxx and 0-maxy respectively
    #
    # Parameters
    #   - canvas - the canvas being used for plotting
    #   - x - value of point in x direction
    #   - maxx - maximum value in x direction (see createGrid)
    #   - y - value of point in y direction
    #   - maxy - maximum value in y directin (see createGrid)

    # Create x, y coordinates ... but remember that graph starts in lower left
    if (x < 0 or x > maxx or y < 0 or y > maxy):
        print("-- drawDots failed because of values out of range")
    else:
        # draw points
        xv = 50+round(400*x/maxx,0)
        yv = 495-(50+round(400*y/maxy,0))
        canvas.setColor(color)
        canvas.drawOval(xv,yv,7,7)


#
#  Testing graphic drawing ... commented out ...
#  ... to run the tests, remove the extra # in front of the remaining lines
#
## Test case 1
## Create the graphics window and get the canvas.
#win = GraphicsWindow(500, 500)
#canvas = win.canvas()
#
## Create a test grid with 100 points in each direction
#createGrid(canvas,100,100)
#
## Draw two lines of 10 points each - one diagonal up the other down
#for t in range (0, 100, 10):
#    drawDots(canvas,t,100,t,100,"red")
#    drawDots(canvas,t,100,100-t,100,"blue")
#
##
## Wait until user kills graph window
#win.wait()
#
## Test case 2
## Create the graphics window and get the canvas.
#win = GraphicsWindow(500, 500)
#canvas = win.canvas()
#
## Create a test grid with 100 points in each direction
#createGrid(canvas,1000,400)
#
## Draw one diagonal line and two curves of points - one based on sin and the other on cosine
#for x in range (1, 1000, 40):
#    drawDots(canvas,x,1000,x,1000,"red")
#    sx = abs(400*sin(x))
#    drawDots(canvas,x,1000,sx,400,"blue")
#    cx = abs(400*cos(x))
#    drawDots(canvas,x,1000,cx,400,"green")
#
##
## Wait until user kills graph window
#win.wait()