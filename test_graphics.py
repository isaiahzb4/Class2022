###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from graphics import *

### Instantiate Graphics Window
win = GraphWin('my window', 1000,1000)

### Start your nested loops here

for x in range(10):

    for y in range(15):

        ### First pick a center point for the circle

        # Then draw the circle
        rect = Rectangle(Point(20, 10),Point(-20, -10))

        # Set the color
        rect.setOutline('red')
        rect.setFill('blue')

        # Then render
        rect.draw(win)

### end your loop here

# Wait for a mouse click to close the Graphics window
win.getMouse()
